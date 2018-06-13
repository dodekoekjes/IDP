from object_detection import ObjectDetection
from arm_controls import Arm
from builder import Builder
from dancing import Dancing
from movement import Movement
from sound_recognition import SoundRecognition
from util.observer import Observer
from bluetooth import connect
import time


class Controller(Observer):
    """This class manages all the modules"""
    def __init__(self):
        """Creates all the modules"""
        print("class: Controller created.")

        self.stances = ["default", "arm", "build", "dance", "battle_stance", ""]
        self.stance = "default"

        self.args = "|"
        self.using_joysticks = False
        self.speed1 = 0
        self.speed2 = 0
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
        self.host = connect.Connect(1, "host", "receive", "10:02:B5:C9:C3:5D", 4, klass=self)
        time.sleep(20)
        self.client = connect.Connect(2, "client", "send", "10:02:B5:C9:C3:5D", 5, klass=self)

        # start bluetooth connection
        self.host.start()
        self.client.start()

        # self.controls()
        self.joystick_controls()

    def update(self, observable, arg):
        """Updates the modules"""
        print("\nUpdate executed")
        print(observable, "\narg:", arg)
        print(observable.__class__)

        if not self.using_joysticks:
            self.args.join(arg+"|")
            if arg == "manual":
                self.using_joysticks = True
            else:  # something controller related
                self.execute(arg)
        else:
            self.joystick_controls(arg)

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
        elif arg == "exit" or arg == "quit":
            print("closing program...")
            exit()

    def joystick_controls(self, args):
        """Commands the controls"""
        right1 = args[0]
        left1 = args[1]
        forward1 = args[2]
        backward1 = args[3]

        right2 = args[4]
        left2 = args[5]
        forward2 = args[6]
        backward2 = args[7]

        speed1 = args[8]
        speed2 = args[9]
        persentage1 = args[10]
        persentage2 = args[11]
        joyval_float1 = args[12]
        joyval_float2 = args[13]

        # convert joystick percentages to servo movespeed
        self.speed1 = 200*(persentage1/100)
        self.speed2 = 200*(persentage2/100)

        # if right1 and forward1:
        # # move right-forward
        #
        # elif right1 and backward1:
        # # move right-backward
        #
        # elif left1 and forward1:
        # # move left-forward
        # elif left1 and backward1:
        # # move left backward
        #
        # if right2 and forward2:
        # # move right-forward
        #
        # elif right2 and backward2:
        # # move right-backward
        #
        # elif left2 and forward2:
        # # move left-forward
        # elif left2 and backward2:
        # # move left backward
        for arg in args:
            print("--", arg)

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
