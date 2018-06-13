import socket
from util.observer import Observable


class Receive(Observable):
    def __init__(self, mac_address, port, backlog=1, size=1024):
        """Listen for incoming data"""
        super().__init__()
        self.host_m_a_c_address = mac_address  # own mac address
        self.port = port
        self.backlog = backlog
        self.size = size
        self.data = None

    def notifyObservers(self, arg=None):
        """Notifies the Observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def start(self):
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((self.host_m_a_c_address, self.port))
        s.listen(self.backlog)
        try:
            print("Connection to bluetooth client..")
            client, address = s.accept()
            print("Connection established.\n"
                  "Waiting for bluetooth client message..")
            while True:
                data = client.recv(self.size)
                if data:
                    print(data)
                    client.send(data)
                    self.data = data
                    if str(data) == "quit":
                        raise Exception("received: quit")
                    else:
                        self.notifyObservers(data)
        except:
            print("\nClosing socket..")
            try:
                client.close()
            except NameError:
                print("ERROR: Connection terminated")
            s.close()


if __name__ == '__main__':
    test = Receive('10:02:B5:C9:C3:5D', 4)
    test.start()
