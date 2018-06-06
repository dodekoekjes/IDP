import sys
import time
import traceback
import readchar
import ax12
# import execute
from .util.observer import Observable


class Movement(Observable):
    """Manages movement controls"""

    def __init__(self, num_legs=6, leg_joints=3):
        """Init"""
        super().__init__()
        print("class: MovementControls created.")
        self.legs = [self.Leg(i, leg_joints) for i in range(num_legs)]
        self.direction = num_legs % 2

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        """Commands the class methods"""
        self.printlegs()
        user_input = input("\nwhat function would you like to execute? "
                           "(walk/battlestance|battle/dab/manual)\n")
        print("Executing:", user_input)


        if user_input == "walk":
            self.walk()
        elif user_input == "battlestance" or user_input == "battle":
            self.battlestance()
        elif user_input == "dab":
            self.dab()
        elif user_input == "manual":
            self.manual()
        else:
            print("Command does not exist.")

        print("\nFalling back to previous prompt..")

        self.notifyObservers()

        # execute.movement()
        #result = call_python_version("2.7", "execute", movement, [])
        #print(result)

    def printlegs(self):
        print("\nServos:", [l.servos for l in self.legs] )

    def walk(self, numsteps=10):
        for l in self.legs:
            l.reset()

        for _ in range(numsteps):
            for l in self.legs:  # raise legs
                if l.direction == 0:
                    continue
                l.raiseleg()
            time.sleep(1)
            for l in self.legs:  # walking
                l.step()
            time.sleep(1)

            for i in range(13):
                print("Servo " + str(i + 1) + ": " + str(ax12.Ax12().readPosition(i + 1)))

    # Dab
    def dab(self, times=3):
        times*=2
        speed = 200
        leg3, leg4 = self.legs[2], self.legs[3]
        i = 0
        count = 0
        while count<times:
            count+=1
            if i == 0:
                leg3.moveservo(leg3.servos[0], 650, speed)
                leg3.moveservo(leg3.servos[1], 300, speed)
                leg3.moveservo(leg3.servos[2], 900, speed)

                leg4.moveservo(leg4.servos[0], 400, speed)
                leg4.moveservo(leg4.servos[1], 300, speed)
                leg4.moveservo(leg4.servos[2], 650, speed)
                i = 1

            elif i == 1:
                leg3.moveservo(leg3.servos[0], 450, speed)
                leg3.moveservo(leg3.servos[1], 200, speed)
                leg3.moveservo(leg3.servos[2], 400, speed)

                leg4.moveservo(leg4.servos[0], 250, speed)
                leg4.moveservo(leg4.servos[1], 200, speed)
                leg4.moveservo(leg4.servos[2], 400, speed)
                i = 0

            time.sleep(1)

    def manual(self):
        print("  Keys: [Q] [A] [W] [S] [E] [D] [R] [.]")
        mv_delta = 30
        speed = 200
        s1 = 350
        s2 = 400  # 150
        s3 = 400  # 150

        for l in self.legs:
            l.reset()
        time.sleep(0.5)

        while True:
            # Read a key
            key = readchar.readkey()

            try:
                if key in "qa":
                    if key == 'q' and s1 > 150:
                        s1 -= mv_delta
                    elif key == 'a' and s1 < 550:
                        s1 += mv_delta
                    for i in range(6):
                        servo_id = i * 3 + 1
                        self.legs[i].moveservo(servo_id, s1, speed)
                elif key in "zx":
                    if key == "z":
                        s1 -= mv_delta
                    if key == "x":
                        s1 += mv_delta
                    for i in range(3, 6):
                        servo_id = i * 3 + 1
                        self.legs[i].moveservo(servo_id, s1, speed)

                elif key in "ws":
                    if key == 'w' and s2 > 150:
                        s2 -= mv_delta
                    elif key == 's' and s2 < 500:
                        s2 += mv_delta
                    for i in range(6):
                        servo_id = i * 3 + 2
                        self.legs[i].moveservo(servo_id, s2, speed)
                elif key in "ed":
                    if key == 'd' and s3 > 150:
                        s3 -= mv_delta
                    elif key == 'e' and s3 < 625:
                        s3 += mv_delta
                    for i in range(6):
                        # print(i)
                        servo_id = i * 3 + 3
                        self.legs[i].moveservo(servo_id, s3, speed)
                elif key == "r":
                    for l in self.legs:  # raise legs
                        if l.direction == 0:
                            continue
                        l.raiseleg()
                    time.sleep(0.2)
                    for l in self.legs:  # walking
                        l.step()
                    time.sleep(0.2)
                elif key == '.':
                    break
            except:
                print("Exception in code:")
                traceback.print_exc(file=sys.stdout)
                print("Continuing...")
                continue

    def battlestance(self):
        speed = 150

        # Reset
        for l in self.legs:
            l.reset()
        time.sleep(1)

        leg1, leg6 = self.legs[0], self.legs[5]
        leg2, leg5 = self.legs[1], self.legs[4]
        leg3, leg4 = self.legs[2], self.legs[3]

        # Move middle legs up
        leg5.moveservo(leg5.servos[1], 150, speed)
        leg5.moveservo(leg5.servos[2], 150, speed)

        leg2.moveservo(leg2.servos[1], 150, speed)
        leg2.moveservo(leg2.servos[2], 150, speed)

        # Leg 1
        leg1.moveservo(leg1.servos[0], 350, speed)
        leg1.moveservo(leg1.servos[1], 200, speed)
        leg1.moveservo(leg1.servos[2], 250, speed)

        # Leg 6
        leg6.moveservo(leg6.servos[0], 350, speed)
        leg6.moveservo(leg6.servos[1], 200, speed)
        leg6.moveservo(leg6.servos[2], 250, speed)

        time.sleep(0.5)

        # Leg 2,5 forward
        leg2.moveservo(leg2.servos[0], 550, 200)
        leg5.moveservo(leg5.servos[0], 150, 200)

        time.sleep(0.5)

        leg2.moveservo(leg2.servos[2], 500, 200)
        leg5.moveservo(leg5.servos[2], 500, 200)
        leg3.moveservo(leg3.servos[2], 550, 200)
        leg4.moveservo(leg4.servos[2], 550, 200)

        time.sleep(0.5)

        leg2.moveservo(leg2.servos[1], 500, 200)
        leg5.moveservo(leg5.servos[1], 500, 200)
        leg3.moveservo(leg3.servos[1], 600, 200)
        leg4.moveservo(leg4.servos[1], 600, 200)

        time.sleep(1)

        # Leg 3
        leg3.moveservo(leg3.servos[0], 450, speed)
        leg3.moveservo(leg3.servos[1], 200, speed)
        leg3.moveservo(leg3.servos[2], 400, speed)

        # Leg 4
        leg4.moveservo(leg4.servos[0], 250, speed)
        leg4.moveservo(leg4.servos[1], 200, speed)
        leg4.moveservo(leg4.servos[2], 400, speed)

        time.sleep(1)


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

            self.forwardangle = 400  # 50 forward
            self.backwardangle = 300  # 50 backward

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
                # time.sleep(0.5)

        def step(self):
            speed = 200

            if self.direction == 1:
                self.moveservo(self.servos[1], 150, speed)
                self.moveservo(self.servos[2], 150, speed)

                self.moveservo(self.servos[0], self.forwardangle, speed)
                self.moveservo(self.servos[1], 400, speed)
                self.moveservo(self.servos[2], 400, speed)

                time.sleep(0.2)  # was first 0.5

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
