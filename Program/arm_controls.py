from util.observer import Observable
# import arm
# import ax12


class Arm(Observable):
    """Makes the robot dance"""
    def __init__(self):
        """Init: super = Observable"""
        super().__init__()
        print("class: Dancing created.")
        # self.arm = arm.Arm3Link()

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        print("Arm command executed!")
        self.notifyObservers()

        # replace test to proper function name
        # self.test()
        # ----------

        # result = call_python_version("2.7", "python2_test", "my_function", ["Mr", "Wolf"])
        # print("python2.7 test:", result)

    # def test(self):
    #     # replace test() for real code
    #     arm.test()
