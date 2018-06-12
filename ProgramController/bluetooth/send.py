import socket


class Send:
    def __init__(self, mac_address, port):
        """Send raw data"""
        self.server_m_a_c_address = mac_address  # server mac address
        self.port = port
        try:
            self.s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            self.s.connect((self.server_m_a_c_address, self.port))
        except OSError as e:
            print("ERROR:", e.args)

    def controller_input(self, arg):
        """Sends controller input"""
        if arg == "quit":
            self.s.close()
        try:
            self.s.send(bytes(arg, 'UTF-8'))
        except socket.error as e:
            print("ERROR:", e.args)

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


if __name__ == '__main__':
    test = Send('10:02:B5:C9:C3:5D', 4)
    test.console()
