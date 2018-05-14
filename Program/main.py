from controller import Controller


class Main:
    """This is the main class"""
    def __init__(self):
        """initializes the class"""
        self.log = []

    def start(self):
        """Starts the controller"""
        Controller()


main = Main()
main.start()

