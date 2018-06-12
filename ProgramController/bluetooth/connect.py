import threading

from .receive import Receive
from .send import Send


class Connect(threading.Thread):
    def __init__(self, threadID, name, param: str, mac_address: str, port: int):
        """Interact with another bluetooth device using multi-threading"""
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.param = param
        self.macc_address = mac_address
        self.port = port

    def run(self):
        """Do something when thread starts"""
        print("Starting", self.name, ": Thread ID =", self.threadID)
        print("Executing", self.param)
        connection = None
        if self.param == "send":
            connection = Send(self.macc_address, self.port)
            connection.controller_input("1 {X:Y:B} 2{X:Y:B}")
            connection.console()  # don't forget to comment this out
        elif self.param == "receive":
            connection = Receive(self.macc_address, self.port)
            connection.start()
        else:
            print("you did not select the proper command\nCommands\n -- send\n -- receive")
