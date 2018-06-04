from util.observer import Observable


class SoundRecognition(Observable):
    """Recognise sound"""
    def __init__(self):
        """Init"""
        super().__init__()
        print("class: SoundRecognition created.")

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        pass

    def listen(self):
        pass
