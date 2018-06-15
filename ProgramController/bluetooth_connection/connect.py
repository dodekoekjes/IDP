import threading

from .receive import Receive


class Connect(threading.Thread):
    def __init__(self, threadID, name, mac_address: str, port: int, klass):
        """Interact with another bluetooth device using multi-threading"""
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.param = param
        self.macc_address = mac_address
        self.port = port
        self.host = None
        self.klass = klass

    def run(self):
        """Do something when thread starts"""
        print("Starting", self.name, ": Thread ID =", self.threadID)
        self.host = Receive(self.macc_address, self.port)
        self.host.addObserver(self.klass)
        self.host.start()
