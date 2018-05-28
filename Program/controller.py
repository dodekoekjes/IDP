from object_detection import ObjectDetection
from controls import ArmControls
from builder import Builder
from dancing import Dancing
from controls import MovementControls
from sound_recognition import SoundRecognition
from util.observer import Observer
import readchar


class Controller(Observer):
    """This class manages all the modules"""
    def __init__(self):
        """Creates all the modules"""
        print("class: Controller created.")

        self.input = None

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

        # test
        # self.arm.notifyObservers()
        # self.builder.notifyObservers()
        # self.dancing.notifyObservers()
        # self.direction.notifyObservers()
        # self.movement.notifyObservers()
        # self.sound.notifyObservers()
        self.controls()

    def update(self, observable, arg):
        """Updates the modules"""
        print("Update executed")
        print(observable, " : ", arg)

    def controls(self):
        """Command the controls"""
        while True:
            user_input = input("pres a key:\n")
            print("you typed: ", user_input)
            user_input.lower()

            if user_input == "help" or user_input == "h" or user_input == "0":
                self.input = user_input
                self.commandsHelp()
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
            else:
                self.input = user_input
                self.commandsHelp()
    def commandsHelp(self):
        print("\nThere is no command: ", self.input, "\nCommands:\n"
                                                     " [0] help"
                                                     " [1] arm\n"
                                                     " [2] builder\n"
                                                     " [3] dancing\n"
                                                     " [4] direction\n"
                                                     " [5] movement\n"
                                                     " [6] sound")
        self.input = None
