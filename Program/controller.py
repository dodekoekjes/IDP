from object_detection import ObjectDetection
from arm_controls import Arm
from builder import Builder
from dancing import Dancing
from movement import Movement
from sound_recognition import SoundRecognition
from util.observer import Observer
from bluetooth_connection import *
import time
import robot


class Controller(Observer):
    """This class manages all the modules"""
    def __init__(self):
        """Creates all the modules"""
        print("class: Controller created.")

        self.stances = ["default", "arm", "build", "dance", "battle_stance", ""]
        self.stance = "default"

        self.args = "|"
        self.using_joysticks = False
        self.speed1_x = 0
        self.speed1_y = 0
        self.speed2_x = 0
        self.speed2_y = 0
        self.arm = Arm()
        self.builder = Builder()
        self.dancing = Dancing()
        self.direction = ObjectDetection()
        self.movement = Movement()
        self.sound = SoundRecognition()
        self.reset = False
        self.drive = False

        # initialize bluetooth_connection connection
        self.host = connect.Connect(1, "host", 'B8:27:EB:36:3E:F8', 4, self)
        self.host.start()
        time.sleep(20)
        self.client = send.Send(2, "client", 'B8:27:EB:DE:5F:36', 5)
        self.client.start()
        time.sleep(10)

        self.msg_received = False
        # Add controller as observer to classes
        self.arm.addObserver(self)
        self.builder.addObserver(self)
        self.dancing.addObserver(self)
        self.direction.addObserver(self)
        self.movement.addObserver(self)
        self.sound.addObserver(self)

        self.robot = robot.Robot(6, 3)

        self.list = [self.arm, self.builder, self.dancing, self.direction, self.movement, self.sound]



        # self.controls()
        # self.joystick_controls()

    def has_received(self):
        try:
            self.client.controller_input("received")
        except:
            self.client = send.Send(2, "client", 'B8:27:EB:DE:5F:36', 5)
            self.client.start()
            time.sleep(10)
            self.has_received()

    def update(self, observable, arg):
        """Updates the modules"""
        print("\nUpdate executed")
        print(observable, "\narg:", arg)
        print(observable.__class__)

        if arg[0] == 0:
            arg[0] = "manual"
        elif arg[0] == 1:
            arg[0] = "battlestance"
        elif arg[0] == 2:
            arg[0] = "dab"
        elif arg[0] == 3:
            arg[0] = "ball"
        elif arg[0] == 4:
            arg[0] = "reset"
        elif arg[0] == 5:
            arg[0] = "dance"
        elif arg[0] == 6:
            arg[0] = "linedance"
        elif arg[0] == 7:
            arg[0] = "highstep"
        elif arg[0] == 8:
            arg[0] = "lowstep"
        elif arg[0] == 9:
            arg[0] = "drive"

        self.has_received()

        print("arg[0] converted:", arg[0])

        self.joystick_contsrols(arg)

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

    def joystick_contsrols(self, args):
        """Commands the controls"""
        joyval_float1_x = args[1]
        joyval_float1_y = args[2]
        button1 = args[3] # Left Joystick
        joyval_float2_x = args[4]
        joyval_float2_y = args[5]
        button2 = args[6] # Right Joystick

        self.speed1_x = abs(200*joyval_float1_x)
        self.speed1_y = abs(200*joyval_float1_y)
        self.speed2_x = abs(200*joyval_float2_x)
        self.speed2_y = abs(200*joyval_float2_y)

        # test
        for arg in args:
            print("--", arg)
        if args[0] == "manual":
            if self.reset:
                self.robot.reset()
                self.reset = False
            self.robot.manual(joyval_float1_x, joyval_float1_y, button1, joyval_float2_x, joyval_float2_y, button2)
            self.drive = False
        elif args[0] == "highstep":
            if self.reset:
                self.reset = False
            self.robot.toggleStairs()
            self.robot.manual(joyval_float1_x, joyval_float1_y, button1, joyval_float2_x, joyval_float2_y, button2)
        elif button1 or args[0] == "reset":
            self.robot.reset()
        elif args[0] == "battlestance":
            self.robot.battlestance()
            self.drive = False
        elif args[0] == "drive" or button2:

            self.reset = True
            if not self.drive:
                self.robot.drive(self.drive)
                self.drive = True
            else:
                self.robot.drive(self.drive, joyval_float2_x, joyval_float2_y)

        elif args[0] == "dab":
            self.robot.dab()
        elif args[0] == "dance":
            self.robot.dance()
            self.reset = True
        else:
            print("do something else -> line 166 controller.py")

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
