import socket
from util.observer import Observable
import struct


class Receive(Observable):
    def __init__(self, mac_address, port, backlog=1, size=1024):
        """Listen for incoming data"""
        super().__init__()
        self.host_m_a_c_address = mac_address  # own mac address
        self.port = port
        self.backlog = backlog
        self.size = size
        self.data = None

        self.INT = 0x00
        self.UINT = 0x01
        self.STR = 0x02
        self.BOOL = 0x03
        self.FLOAT = 0x04

    def notifyObservers(self, arg=None):
        """Notifies the Observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def start(self):
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((self.host_m_a_c_address, self.port))
        s.listen(self.backlog)
        try:
            print("setting up bluetooth host")
            client, address = s.accept()
            print("Host setup successful.")
            while True:
                print("Waiting for bluetooth client message..")
                data = client.recv(self.size)
                if data:
                    print("raw",data)
                    #client.sendall(data)
                    self.data = self.convert(data)

                    if str(data) == "quit":
                        raise Exception("received: quit")
                    else:
                        self.notifyObservers(self.data)
        except:
            print("\nClosing socket..")
            try:
                client.close()
            except NameError:
                print("ERROR: Connection terminated")
            s.close()

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
