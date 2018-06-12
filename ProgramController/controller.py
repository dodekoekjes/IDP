from bluetooth import connect
from utils.observer import Observer


class Controller(Observer):
    def __init__(self):
        """Creates all the modules"""

        # setup host
        self.host = connect.Connect(1, "host", "receive", '10:02:B5:C9:C3:5D', 4)

        # setup client
        self.client = connect.Connect(2, "client", "send", '10:02:B5:C9:C3:5D', 5)

        self.start()

    def start(self):
        """Starts modules and components"""
        # Start new threads
        self.host.start()
        self.client.start()

    def update(self, observable, arg):
        """updates the modules"""
        print(observable, "argument:", arg)
