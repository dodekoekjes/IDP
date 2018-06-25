import sys, traceback
import time
import ax12


class Leg:

    def __init__(self, legnum, numservos):
        self.servos = [legnum * numservos + i + 1 for i in range(3)]
        self.direction = legnum % 2
        self.numlegs = legnum
        self.side = None
        if legnum < 3:
            side = 'l'
        else:
            self.side = 'r'

        # (350 is default)
        self.forwardangle = 450  # 100 forward
        self.backwardangle = 300  # 100 backward

        if self.side == 'r':
            self.forwardangle, self.backwardangle = self.backwardangle, self.forwardangle

    def moveservo(self, servo_idx, angle, speed):
        try:
            ax12.Ax12().moveSpeed(servo_idx, angle, speed)
            time.sleep(0.005)
        except IndexError:
            print(str(servo_idx) + " Out of range")
            return
        except:
            print("\nCould not move Servo " + str(servo_idx))
            # traceback.print_exc(file=sys.stdout)

    def raiseleg(self):
        speed = 200
        sleeptime = 0.02
        if self.direction == 1:
            self.moveservo(self.servos[1], 200, speed)
            time.sleep(sleeptime)
            self.moveservo(self.servos[2], 200, speed)

    def step(self, reverse, steer=0):
        speed = 150 # 150
    
    if steer == 0:
        fwangle = self.forwardangle
        bwangle = self.backwardangle
    elif steer == 1:
        fwangle = self.forwardangle - 50
        bwangle = self.backwardangle + 50
    elif steer == 2:
        fwangle = self.forwardangle + 50
        bwangle = self.backwardangle - 50

        if reverse:
            if self.direction == 1:
                self.moveservo(self.servos[0], bwangle, speed) # servo 1
                self.moveservo(self.servos[1], 485, speed) # servo 2
                self.moveservo(self.servos[2], 450, speed) # servo 3

                self.direction = 0

            elif self.direction == 0:
                self.moveservo(self.servos[0], fwangle, speed)
                self.moveservo(self.servos[1], 485, speed)
                self.moveservo(self.servos[2], 450, speed)

                self.direction = 1
        else:
            if self.direction == 1:
                self.moveservo(self.servos[0], fwangle, speed)
                self.moveservo(self.servos[1], 485, speed)
                self.moveservo(self.servos[2], 400, speed)

                self.direction = 0

            elif self.direction == 0:
                self.moveservo(self.servos[0], bwangle, speed)
                self.moveservo(self.servos[1], 485, speed)
                self.moveservo(self.servos[2], 400, speed)

                self.direction = 1

    def reset(self):
        speed = 200
        sleeptime = 0.3
        self.moveservo(self.servos[0], 350, speed)  # 1e servo
        time.sleep(sleeptime)
        self.moveservo(self.servos[2], 450, speed)  # 3e servo
        time.sleep(sleeptime)
        self.moveservo(self.servos[1], 450, speed)  # 2e servo
        # time.sleep(sleeptime)
        # time.sleep(1)
