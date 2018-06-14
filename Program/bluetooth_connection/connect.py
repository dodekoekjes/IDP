import threading

from .receive import Receive
from .send import Send


class Connect(threading.Thread):
    def __init__(self, threadID, name, param: str, mac_address: str, port: int, klass):
        """Interact with another bluetooth_connection device using multi-threading"""
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.param = param
        self.macc_address = mac_address
        self.port = port
        self.send = Send(self.macc_address, self.port)
        self.host = None
        self.klass = klass

    def run(self):
        """Do something when thread starts"""
        print("Starting", self.name, ": Thread ID =", self.threadID)
        print("Executing", self.param)
        if self.param == "send":
            self.send = Send(self.macc_address, self.port)
            # self.connection.controller_input("1 {X:Y:B} 2{X:Y:B}")
            # self.connection.console()  # don't forget to comment this out
        elif self.param == "receive":
            self.host = Receive(self.macc_address, self.port)
            self.host.addObserver(self.klass)
            self.host.start()
        else:
            print("you did not select the proper command\nCommands\n -- send\n -- receive")

    def command(self, args=None):
        self.send.controller_input(args)
