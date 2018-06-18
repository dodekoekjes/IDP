from bluetooth import *
from util.observer import Observable
import struct
import threading


class Receive(Observable):
    def __init__(self, mac_address, port, backlog=1, size=1024):
        """Listen for incoming data"""
        super().__init__()
        self.host_m_a_c_address = mac_address  # own mac address
        self.port = port
        self.backlog = backlog
        self.size = size
        self.data = None

        self.server_sock = BluetoothSocket(RFCOMM)
        self.server_sock.bind(("", PORT_ANY))
        self.server_sock.listen(1)

        self.port = self.server_sock.getsockname()[1]

        self.uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

        advertise_service(self.server_sock, "groep12Controller",
                               service_id=self.uuid,
                               service_classes=[self.uuid, SERIAL_PORT_CLASS],
                               profiles=[SERIAL_PORT_PROFILE],
                               # protocols = [ OBEX_UUID ]
                               )

        print("Waiting for connection on RFCOMM channel %d" % self.port)
        self.client_sock, self.client_info = self.server_sock.accept()
        print("Accepted connection from ", self.client_info)

        self.INT = 0x00
        self.UINT = 0x01mp
        self.STR = 0x02
        self.BOOL = 0x03
        self.FLOAT = 0x04

    def notifyObservers(self, arg=None):
        """Notifies the Observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def start(self):
        try:
            while True:
                data = self.client_sock.recv(self.size)
                if len(data) == 0: break
                print("received [%s]" % data)
                self.notifyObservers(self.convert(bytearray(data)))
        except IOError:
            pass

        print("disconnected")

        self.client_sock.close()
        self.server_sock.close()
        print("all done")

    def convert(self, data):
        offset = 0
        arr_bytes = data
        arr = []

        for _ in range(7):
            arr2 = bytearray()
            vtype = arr_bytes[offset]
            vtype2 = ""
            len = 0
            offset += 1

            if vtype == self.INT:
                len = 4
                vtype2 = "<i"
            elif vtype == self.BOOL:
                len = 1
                vtype2 = "?"
            elif vtype == self.FLOAT:
                len = 4
                vtype2 = "<f"

            for _ in range(len):
                arr2.append(arr_bytes[offset])
                offset += 1
            # print(struct.unpack(vtype2, arr2)[0])
            arr.append(struct.unpack(vtype2, arr2)[0])

        return arr


if __name__ == '__main__':
    test = Receive('B8:27:EB:36:3E:F8', 4)
    test.start()
