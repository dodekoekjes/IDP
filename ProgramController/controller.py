from bluetooth import connect
from utils.observer import Observer
from input import Input as CI
import time


class Controller(Observer):
    def __init__(self):
        """Creates all the modules"""

        # setup host
        self.host = connect.Connect(1, "host", "receive", '10:02:B5:C9:C3:5D', 4)

        # setup client
        self.client = connect.Connect(2, "client", "send", '40:2C:F4:E3:63:61', 5)

        self.joystick_input = None
        self.args = "|"

        self.start()

    def start(self):
        """Starts modules and components"""
        # Start new threads
        self.host.start()
        time.sleep(10)
        self.client.start()
        self.controls()

    def controls(self):
        while True:
            controller_input = CI()

            # add "dev" to run on computer
            self.joystick_input = controller_input.read("dev")
            print("Joystick Input:", self.joystick_input)

    def update(self, observable, arg):
        """updates the modules"""
        print(observable, "argument:", arg)
        self.args.join(arg+"|")
