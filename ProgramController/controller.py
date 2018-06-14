from bluetooth_connection import connect
from util.observer import Observer
from input import Input as CI
import time
import math


class Controller(Observer):
    def __init__(self):
        """Creates all the modules"""

        # setup host
        self.host = connect.Connect(1, "host", "receive", 'B8:27:EB:DE:5F:36', 5, klass=self)
        time.sleep(10)
        # setup client
        self.client = connect.Connect(2, "client", "send", 'B8:27:EB:36:3E:F8', 4, klass=self)

        self.controller_input = None
        self.args = []
        self.stance = "manual"
        self.stances = ["manual", "dance", "battlestance", "dab", "reset"]
        self.start()

    def start(self):
        """Starts modules and components"""
        # Start new threads
        self.host.start()
        self.client.start()
        self.controls()

    def controls(self):
            command = []
            self.controller_input = CI()
            # add "dev" to run on computer
            if self.stance == "manual":

                output = self.controller_input.read("dev")  # remove dev when on raspberry pi
                print("Joystick Input:", self.controller_input)

                # joystick 1
                x1 = int(output[0])
                y1 = int(output[1])
                b1 = bool(output[2])

                # joystick 2
                x2 = int(output[3])
                y2 = int(output[4])
                b2 = bool(output[5])

                # processing inputs
                right1 = False
                left1 = False
                forward1 = False
                backward1 = False

                right2 = False
                left2 = False
                forward2 = False
                backward2 = False

                if 600 < x1 < 1023:  # X+
                    # move right
                    right1 = True

                elif 0 < x1 < 423:  # X-
                    # move left
                    left1 = True

                if 600 < y1 < 1023:  # Y+
                    # move forward
                    forward1 = True

                elif 0 < y1 < 423:  # Y-
                    # move backward
                    backward1 = True

                if 600 < x2 < 1023:  # X+
                    # move right
                    right2 = True

                elif 0 < x2 < 423:  # X-
                    # move left
                    left2 = True

                if 600 < y2 < 1023:  # Y+
                    # move forward
                    forward2 = True
                elif 0 < y2 < 423:  # Y-
                    # move backward
                    backward2 = True
                # if b1:
                #     # button pressed
                # if b2:
                #     # button pressed
                speed1 = 0
                if right1 and forward1:
                    try:
                        speed1 = math.sqrt(math.pow((x1 - 600), 2) + math.pow((y1 - 600), 2))
                    except:
                        speed1 = 0
                elif right1 and backward1:
                    try:
                        speed1 = math.sqrt(math.pow((x1 - 600), 2) + math.pow((423 - y1), 2))
                    except:
                        speed1 = 0
                elif left1 and forward1:
                    try:
                        speed1 = math.sqrt(math.pow((423 - x1), 2) + math.pow((y1 - 600), 2))
                    except:
                        speed1 = 0
                elif left1 and backward1:
                    try:
                        speed1 = math.sqrt(math.pow((423 - x1), 2) + math.pow((423 - y1), 2))
                    except:
                        speed1 = 0

                speed2 = 0
                if right2 and forward2:
                    try:
                        speed2 = math.sqrt(math.pow((x2 - 600), 2) + math.pow((y2 - 600), 2))
                    except:
                        speed2 = 0
                elif right2 and backward2:
                    try:
                        speed2 = math.sqrt(math.pow((x2 - 600), 2) + math.pow((423 - y2), 2))
                    except:
                        speed2 = 0
                elif left2 and forward2:
                    try:
                        speed2 = math.sqrt(math.pow((423 - x2), 2) + math.pow((y2 - 600), 2))
                    except:
                        speed2 = 0
                elif left2 and backward2:
                    try:
                        speed2 = math.sqrt(math.pow((423 - x2), 2) + math.pow((423 - y2), 2))
                    except:
                        speed2 = 0
                speed1_percentage = (speed1*100/423)  # = %
                speed2_percentage = (speed2*100/423)  # = %

                # -1 - 1
                ## Divide 1 by half the maximum possible value
                MULTIPLIER = 1 / 511.5


                ## Multiply afformentioned position by the MULTIPLIER and subtract 1
                joyval_float1_x = MULTIPLIER * x1 - 1
                joyval_float1_y = MULTIPLIER * y1 - 1
                joyval_float2_x = MULTIPLIER * x2 - 1
                joyval_float2_y = MULTIPLIER * y2 -1

                command = ["manual", joyval_float1_x, joyval_float1_y, b1, joyval_float2_x, joyval_float2_y, b2]
                print("Command:")
                for item in command:
                    print("-- " + str(item))



                # testing
                print(x1, y1, b1, x2, y2, b2)

            self.client.command(command)

    def update(self, observable, arg):
        """updates the modules"""
        print(observable, "argument:", arg)

        if arg == "received":
            self.controls()

        if arg[0] in self.stances:
            self.stance = arg[0]
        self.args.append(arg)
