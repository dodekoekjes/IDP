from pyax12.connection import Connection
# import RPi.GPIO as gpio
# from ax12 import Ax12
from util.observer import Observable


class MovementControls(Observable):
    """Manages movement controls"""
    def __init__(self):
        """Init"""
        super().__init__()
        print("class: MovementControls created.")
#        ax = Ax12()

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        pass


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
