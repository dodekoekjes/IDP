import threading
import time


class PrintInput(threading.Thread):
    def __init__(self,threadID, name, vrx_pos1, vry_pos1, b_pressed1, vrx_pos2, vry_pos2, b_pressed2, delay=0.5):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.vrx_pos1 = vrx_pos1
        self.vry_pos1 = vry_pos1
        self.b_pressed1 = b_pressed1
        self.vrx_pos2 = vrx_pos2
        self.vry_pos2 = vry_pos2
        self.b_pressed2 = b_pressed2
        self.delay = delay

    def __del__(self):
        del self

    def execute(self):
        time.sleep(self.delay)
        print(
            "Joystick 1:"
            "VRx : {}  "
            "VRy : {}  "
            "pressed : {}  "
            "Joystick 2:"
            "VRx : {}  "
            "VRy : {}  "
            "pressed : {}".format(
                self.vrx_pos1,
                self.vry_pos1,
                self.b_pressed1,
                self.vrx_pos2,
                self.vry_pos2,
                self.b_pressed2))

    def start(self):
        self.execute()
        self.__del__()