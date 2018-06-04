from util.observer import Observable


class Builder(Observable):
    """Build with objects"""
    def __init__(self):
        """Init: super = Observable"""
        super().__init__()
        print("class: Builder created.")

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        pass

    def construct(self):
        pass

    def deconstruct(self):
        pass
