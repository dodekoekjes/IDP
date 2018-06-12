from object_detection import ObjectDetection
from arm_controls import Arm
from builder import Builder
from dancing import Dancing
from movement import Movement
from sound_recognition import SoundRecognition
from util.observer import Observer
from bluetooth import connect


class Controller(Observer):
    """This class manages all the modules"""
    def __init__(self):
        """Creates all the modules"""
        print("class: Controller created.")

        self.stances = ["default", "arm", "build", "dance", "battle_stance", ""]
        self.stance = "default"



        self.arm = Arm()
        self.builder = Builder()
        self.dancing = Dancing()
        self.direction = ObjectDetection()
        self.movement = Movement()
        self.sound = SoundRecognition()

        # Add controller as observer to classes
        self.arm.addObserver(self)
        self.builder.addObserver(self)
        self.dancing.addObserver(self)
        self.direction.addObserver(self)
        self.movement.addObserver(self)
        self.sound.addObserver(self)

        self.list = [self.arm, self.builder, self.dancing, self.direction, self.movement, self.sound]

        # initialize bluetooth connection
        self.host = connect.Connect(1, "host", "receive", "10:02:B5:C9:C3:5D", 4)
        self.client = connect.Connect(2, "client", "send", "10:02:B5:C9:C3:5D", 5)

        # start bluetooth connection
        self.host.start()
        self.client.start()

        # self.controls()

    def update(self, observable, arg):
        """Updates the modules"""
        print("\nUpdate executed")
        print(observable, "\narg:", arg)
        print(observable.__class__)

        if arg == "something not controller related":
            print("do something else")
        else:  # something controller related
            self.execute(arg)
            # self.host.read_output()

    def execute(self, arg):
        if arg == "arm":
            self.arm.command()

        elif arg == "builder":
            self.builder.command()

        elif arg == "dancing":
            self.dancing.command()
        elif arg == "direction":
            self.direction.command()
        elif arg == "movement":
            self.movement.command()
        elif arg == "sound":
            self.sound.command()
        elif arg == "exit":
            print("closing program...")
            exit()

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
            elif user_input == "exit" or user_input == "shutdown" or user_input == ".":
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
                  " [4] detection\n"
                  " [5] movement\n"
                  " [6] sound\n"
                  " [.] exit/shutdown")
        else:
            print("\nThere is no command: ", user_input,
                  "\nCommands:\n"
                  " [0] help\n"
                  " [1] arm\n"
                  " [2] builder\n"
                  " [3] dancing\n"
                  " [4] detection\n"
                  " [5] movement\n"
                  " [6] sound\n"
                  " [.] exit/shutdown")

    def default_stance(self):
        pass
