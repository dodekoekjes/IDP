#from ax12 import Ax12
import time
import traceback, sys
from util.observer import Observable
from util.version_control import call_python_version
import execute

class MovementControls(Observable):
    """Manages movement controls"""

    def __init__(self, num_legs=6, leg_joints=3):
        """Init"""
        super().__init__()
        print("class: MovementControls created.")

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        """Commands the class methods"""
        self.locomotion("movement")

        self.notifyObservers()


    def locomotion(self, method):
        """commands the robot walk animation"""
        print("locomotion executed.")
        execute.movement(   )
        #result = call_python_version("2.7", "execute", method, [])
        #print(result)


    def leg(self):
        """Controls a leg"""


class ArmControls(Observable):
    """Manages arm controls"""

    def __init__(self):
        """Init"""
        super().__init__()
        print("class: ArmControls created.")

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        pass

    def move_x(self):
        pass

    def move_y(self):
        pass

    def move_z(self):
        pass

    def open_claw(self):
        pass

    def close_claw(self):
        pass

    def rotate_claw(self):
        pass
