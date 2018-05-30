from object_detection import ObjectDetection
from controls import ArmControls
from builder import Builder
from dancing import Dancing
from controls import MovementControls
from sound_recognition import SoundRecognition
from util.observer import Observer


class Controller(Observer):
    """This class manages all the modules"""
    def __init__(self):
        """Creates all the modules"""
        print("class: Controller created.")

        self.stances = ["default", "arm", "build", "dance", "battle_stance", ""]
        self.stance = "default"

        self.arm = ArmControls()
        self.builder = Builder()
        self.dancing = Dancing()
        self.direction = ObjectDetection()
        self.movement = MovementControls()
        self.sound = SoundRecognition()

        # Add controller as observer to classes
        self.arm.addObserver(self)
        self.builder.addObserver(self)
        self.dancing.addObserver(self)
        self.direction.addObserver(self)
        self.movement.addObserver(self)
        self.sound.addObserver(self)

        self.list = [ self.arm, self.builder, self.dancing, self.direction, self.movement, self.sound]

        # test
        # self.arm.notifyObservers()
        # self.builder.notifyObservers()
        self.dancing.notifyObservers()
        # self.direction.notifyObservers()
        # self.movement.notifyObservers()
        # self.sound.notifyObservers()
        self.controls()

    def update(self, observable, arg):
        """Updates the modules"""
        print("Update executed")
        print(observable, "\narg:", arg)
        print(observable.__class__)

    def controls(self):
        """Command the controls"""
        while True:
            user_input = input("\nType a command:\n")
            print("\nyou typed: ", user_input)
            user_input = user_input.lower()

            if user_input == "help" or user_input == "h" or user_input == "0":
                self.commands_help(user_input)
            elif user_input == "arm" or user_input == "1":
                self.arm.command()
            elif user_input == "builder" or user_input == "2":
                self.builder.command()
            elif user_input == "dancing" or user_input == "3":
                self.dancing.command()
            elif user_input == "direction" or user_input == "4":
                self.direction.command()
            elif user_input == "movement" or user_input == "5":
                self.movement.command()
            elif user_input == "sound" or user_input == "6":
                self.sound.command()
            elif user_input == "exit" or user_input == "shutdown":
                print("closing program...")
                exit()
            else:
                self.commands_help(user_input)

    @staticmethod
    def commands_help(user_input):
        if user_input == "help" or user_input == "h" or user_input == "0":
            print("\nCommands:\n"
                  " [0] help\n"
                  " [1] arm\n"
                  " [2] builder\n"
                  " [3] dancing\n"
                  " [4] direction\n"
                  " [5] movement\n"
                  " [6] sound")
        else:
            print("\nThere is no command: ", user_input,
                  "\nCommands:\n"
                  " [0] help\n"
                  " [1] arm\n"
                  " [2] builder\n"
                  " [3] dancing\n"
                  " [4] direction\n"
                  " [5] movement\n"
                  " [6] sound")

    def default_stance(self):
        pass
