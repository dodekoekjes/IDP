from util.observer import Observable


class Dancing(Observable):
    """Makes the robot dance"""
    def __init__(self):
        """Init: super = Observable"""
        super().__init__()
        self.outer = 0
        print("class: Dancing created.")

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        print("test worked!")
        self.notifyObservers()
