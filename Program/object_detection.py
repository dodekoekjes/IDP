from util.observer import Observable


class ObjectDetection(Observable):
    """Detects objects"""
    def __init__(self):
        """Init"""
        super().__init__()
        print("class: ObjectDetection created.")

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        pass
