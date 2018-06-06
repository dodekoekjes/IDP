from util.observer import Observable
from util.version_control import call_python_version

class Dancing(Observable):
    """Makes the robot dance"""
    def __init__(self):
        """Init: super = Observable"""
        super().__init__()
        print("class: Dancing created.")

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        print("dancing command executed!")
        self.notifyObservers()
        result = call_python_version("2.7", "python2_test", "my_function", ["Mr", "Wolf"])
        print("python2.7 test:", result)

    def dance(self):
        pass
