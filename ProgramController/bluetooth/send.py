import socket
import struct
import time


class Send:
    def __init__(self, mac_address, port):
        """Send raw data"""
        self.server_m_a_c_address = mac_address  # server mac address
        self.port = port
        try:
            self.s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            self.s.connect((self.server_m_a_c_address, self.port))
        except OSError as e:
            print("ERROR: -> init", e.args)

        self.INT = 0x00
        self.UINT = 0x01
        self.STR = 0x02
        self.BOOL = 0x03
        self.FLOAT = 0x04

    def controller_input(self, arg):
        """Sends controller input"""
        if arg[0] == "quit" or arg == "quit":
            self.s.close()

        data = self.convert(arg)
        try:
            self.s.send(data)
        except socket.error as e:
            print("ERROR: -> send", e.args)

    def console(self):
        while 1:
            text = input("Type raw data:\n")
            if text == "quit":
                break
            try:
                self.s.send(bytes(text, 'UTF-8'))
            except socket.error as e:
                    print("ERROR:", e.args)
        self.s.close()

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

        return arr_bytes


if __name__ == '__main__':
    test = Send('10:02:B5:C9:C3:5D', 4)
    test.console()
