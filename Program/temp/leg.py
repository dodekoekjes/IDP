import sys, traceback
import time

import ax12


class Leg:

    def __init__(self, legnum, numservos):
        self.servos = [legnum*numservos+i+1 for i in range(3)]
        self.direction = legnum % 2
        self.numlegs = legnum

    def moveservo(self, servo_idx, angle, speed):
        try:
            ax12.Ax12().moveSpeed(servo_idx, angle, speed)
        except IndexError:
            print(str(servo_idx) + " Out of range")
            return
        except:
            print("\nCould not move Servo " + str(servo_idx))
            # traceback.print_exc(file=sys.stdout)


    def raiseleg(self):
        speed = 200
        sleeptime = 0.01
        if self.direction == 1:
            self.moveservo(self.servos[1], 150, speed)
            time.sleep(sleeptime)
            self.moveservo(self.servos[2], 150, speed)
            time.sleep(sleeptime)
            # time.sleep(0.5)
    
    
    def step(self):
        speed = 200
        sleeptime = 0.01
        if self.direction == 1:
            # self.moveservo(self.servos[1], 150, speed)
            # self.moveservo(self.servos[2], 150, speed)
            # time.sleep(0.5)

            self.moveservo(self.servos[0], 400, speed)
            time.sleep(sleeptime)
            self.moveservo(self.servos[1], 400, speed)
            time.sleep(sleeptime)
            self.moveservo(self.servos[2], 400, speed)
            time.sleep(sleeptime)
            self.direction = 0
        elif self.direction == 0:
            if self.numlegs == 2:
                self.moveservo(self.servos[0], 300, speed)
                time.sleep(sleeptime)
                self.moveservo(self.servos[1], 400, speed)
                time.sleep(sleeptime)
                self.moveservo(self.servos[2], 400, speed)
                time.sleep(sleeptime)
            else:
                self.moveservo(self.servos[0], 500, speed)
                time.sleep(sleeptime)
                self.moveservo(self.servos[1], 400, speed)
                time.sleep(sleeptime)
                self.moveservo(self.servos[2], 400, speed)
                time.sleep(sleeptime)
                
            self.direction = 1
            
            
##        if self.direction == 1:
##            self.moveservo(self.servos[1], 150, 200)
##            self.moveservo(self.servos[2], 150, 200)
##            time.sleep(0.2)
##
##            self.moveservo(self.servos[0], 550, 200)
##            self.moveservo(self.servos[1], 400, 200)
##            self.moveservo(self.servos[2], 300, 200)
##            self.direction = 0
##        elif self.direction == 0:
##            self.moveservo(self.servos[0], 150, 200)
##            self.moveservo(self.servos[1], 400, 200)
##            self.moveservo(self.servos[2], 300, 200)
##            self.direction = 1


    def reset(self):
        sleeptime = 0.01
        self.moveservo(self.servos[0], 350, 200)
        time.sleep(sleeptime)
        self.moveservo(self.servos[1], 400, 200)
        time.sleep(sleeptime)
        self.moveservo(self.servos[2], 400, 200)
        time.sleep(sleeptime)
        time.sleep(0.1)
