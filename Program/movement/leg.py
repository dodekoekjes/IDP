import sys, traceback
import time

import ax12


class Leg:


    def __init__(self, legnum, numservos):
        self.servos = [legnum*numservos+i+1 for i in range(3)]
        self.direction = legnum % 2
        self.numlegs = legnum
        self.side = None
        if legnum < 3:
            side = 'l'
        else:
            self.side = 'r'
        
        self.forwardangle = 400 # 50 forward
        self.backwardangle = 300 # 50 backward
        
        if self.side == 'r':
            self.forwardangle, self.backwardangle = self.backwardangle, self.forwardangle

    def moveservo(self, servo_idx, angle, speed):
        try:
            ax12.Ax12().moveSpeed(servo_idx, angle, speed)
            time.sleep(0.0002)
        except IndexError:
            print(str(servo_idx) + " Out of range")
            return
        except:
            print("\nCould not move Servo " + str(servo_idx))
            traceback.print_exc(file=sys.stdout)


    def raiseleg(self):
        speed = 150
        sleeptime = 0.01
        if self.direction == 1:
            self.moveservo(self.servos[1], 200, speed)
            time.sleep(sleeptime)
            self.moveservo(self.servos[2], 200, speed)
            time.sleep(sleeptime)
            #time.sleep(0.5)
    
    
    def step(self):
        speed = 200
        
        if self.direction == 1:
            self.moveservo(self.servos[1], 150, speed)
            self.moveservo(self.servos[2], 150, speed)

            self.moveservo(self.servos[0], self.forwardangle, speed)
            self.moveservo(self.servos[1], 400, speed)
            self.moveservo(self.servos[2], 400, speed)

            time.sleep(0.2) # was first 0.5
            
            self.direction = 0
        elif self.direction == 0:
            self.moveservo(self.servos[0], self.backwardangle, speed)
            self.moveservo(self.servos[1], 400, speed)
            self.moveservo(self.servos[2], 400, speed)
            
            self.direction = 1


    def reset(self):
        speed = 200
        sleeptime = 0.1
        self.moveservo(self.servos[0], 350, speed)
        time.sleep(sleeptime)
        self.moveservo(self.servos[1], 400, speed)
        time.sleep(sleeptime)
        self.moveservo(self.servos[2], 400, speed)
        time.sleep(sleeptime)
        time.sleep(1)
