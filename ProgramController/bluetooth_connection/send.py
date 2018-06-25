from bluetooth import *
import struct
import time
import sys
import threading


class Send(threading.Thread):
    def __init__(self, threadID, name, mac_address, port):
        """Send raw data"""
        super().__init__()
        self.server_m_a_c_address = mac_address  # server mac address
        self.port = port

        self.addr = self.server_m_a_c_address #'10:02:B5:C9:C3:5D'
        self.uuid = ""
        self.service_matches = None
        self.first_match = None
        self.host = ""

        self.id = threadID
        self.threadName = name

        self.INT = 0x00
        self.UINT = 0x01
        self.STR = 0x02
        self.BOOL = 0x03
        self.FLOAT = 0x04
        self.sock = BluetoothSocket(RFCOMM)

    def run(self):

        if self.addr is None:
            print("no device specified.  Searching all nearby bluetooth_connection devices for")
            print("the Controller service")
        else:
            # self.addr = sys.argv[1]
            print("Searching for Controller on %s" % self.addr)

        # search for the SampleServer service
        self.uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
        self.service_matches = find_service(uuid=self.uuid, address=self.addr)

        if len(self.service_matches) == 0:
            print("couldn't find the Controller service =(")
            sys.exit(0)

        self.first_match = self.service_matches[0]
        self.port = self.first_match["port"]
        self.name = self.first_match["name"]
        self.host = self.first_match["host"]

        print("connecting to \"%s\" on %s" % (self.name, self.host))
        self.sock = BluetoothSocket(RFCOMM)
        self.sock.connect((self.host, self.port))

    def controller_input(self, arg):
        """Sends controller input"""
        if arg[0] == "quit" or arg == "quit":
            self.s.close()
            self.sock.close()
        # Create the client socket


        #print("connected.  type stuff")
        self.sock.send(self.convert(arg))

    #def console(self):
    #    # Create the client socket
    #    self.sock = BluetoothSocket(RFCOMM)
    #    self.sock.connect((self.host, self.port))
#
    #    print("connected.  type stuff")
    #    while True:
    #        data = input()
    #        if len(data) == 0:
    #            break
    #        self.sock.send(data)
#
    #    self.sock.close()

    def convert(self, arg):
        if arg[0] == "manual":
            arg[0] = 0
        elif arg[0] =="battlestance":
            arg[0] = 1
        elif arg[0] == "dab":
            arg[0] = 2
        elif arg[0] == "ball":
            arg[0] = 3
        elif arg[0] == "reset":
            arg[0] = 4
        elif arg[0] == "dance":
            arg[0] = 5

        arr = arg
        arr_bytes = bytearray()
        for v in arr:
            # print(type(v) is bool)
            vtype = ""
            if type(v) is int:
                vtype = "<i"
                arr_bytes.append(self.INT)
            elif type(v) is bool:
                vtype = "?"
                arr_bytes.append(self.BOOL)
            elif type(v) is float:
                vtype = "<f"
                arr_bytes.append(self.FLOAT)

            val = struct.pack(vtype, v)
            for b in val:
                arr_bytes.append(b)

        print(arr_bytes)

        return bytes(arr_bytes)


if __name__ == '__main__':
    test = Send('10:02:B5:C9:C3:5D', 4)
    test.console()
