from leg import Leg
import time
import ax12
import readchar
import sys, traceback
import RPi.GPIO as GPIO


class Robot:

    def __init__(self, numlegs, legjoints):
        self.legs = [Leg(i, legjoints) for i in range(numlegs)]
        self.direction = numlegs % 2
        self.l = Leg(i, legjoints)

    def printlegs(self):
        print([l.servos for l in self.legs])

    # Walking function
    def walk(self, numsteps):
        # Servo Speed
        speed = 200

        # Leg reset
        for i in range(6):
            # self.legs[i].moveservo(id, s1, speed)
            for s in range(3):
                if s == 0:
                    self.legs[i].moveservo(s + 1, 450, speed)
                else:
                    self.legs[i].moveservo(s + 1, 350, speed)
                time.sleep(0.5)

        print("Waiting for reset")

        for _ in range(numsteps):
            for l in self.legs:  # Raise legs
                if l.direction == 0:
                    continue
                l.raiseleg()
            time.sleep(1)
            for l in self.legs:  # Walking
                l.step(False)
            time.sleep(1)

            for i in range(13):
                print ("Servo " + str(i + 1) + ": " + str(ax12.Ax12().readPosition(i + 1)))

    # Dab
    def dab(self):
        speed = 200
        leg3, leg4 = self.legs[2], self.legs[3]
        i = 0

        while True:
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

    # Show load
    def showLoad(self):
        print("\n --- LOAD ON SERVOS ---")
        for a in ax12.Ax12().learnServos(1, 254):
            print("Servo " + str(a) + ": " + str(ax12.Ax12().readLoad(a)))
            time.sleep(0.02)
        time.sleep(1)

    # Show positions
    def showPositions(self):
        print("\n --- SERVO POSITIONS ---")
        for a in ax12.Ax12().learnServos(1, 254):
            print("Servo " + str(a) + ": " + str(ax12.Ax12().readPosition(a)))
            time.sleep(0.02)
        time.sleep(1)

    # Controls
    def manual(self):
        mv_delta = 30
        speed = 200
        s1 = 350
        s2 = 400  # 150
        s3 = 400  # 150

        print("HEINZ: Manual mode activated")

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
                        id = i * 3 + 1
                        self.legs[i].moveservo(id, s1, speed)
                elif key in "ws":
                    if key == 'w' and s2 > 150:
                        s2 -= mv_delta
                    elif key == 's' and s2 < 500:
                        s2 += mv_delta
                    for i in range(6):
                        id = i * 3 + 2
                        self.legs[i].moveservo(id, s2, speed)
                elif key in "ed":
                    if key == 'd' and s3 > 150:
                        s3 -= mv_delta
                    elif key == 'e' and s3 < 625:
                        s3 += mv_delta
                    for i in range(6):
                        # print i
                        id = i * 3 + 3
                        self.legs[i].moveservo(id, s3, speed)
                elif key == "r":  # Walking
                    for l in self.legs:  # raise legs
                        if l.direction == 0:
                            continue
                        l.raiseleg(200)

                    time.sleep(0.4)
                    for l in self.legs:
                        l.step(False)
                        time.sleep(0.009)
                    time.sleep(1)
                elif key == "f":
                    for l in self.legs:
                        if l.direction == 0:
                            continue
                        l.raiseleg(200)

                    time.sleep(0.4)

                    for l in self.legs:
                        l.step(False, 1)
                        time.sleep(0.009)
                    time.sleep(1)
                elif key == "v":
                    for l in self.legs:
                        if l.direction == 0:
                            continue
                        l.raiseleg(200)

                    time.sleep(0.4)
                    for l in self.legs:
                        l.step(False, 2)
                        time.sleep(0.009)
                    time.sleep(1)
                elif key == "c": # Walk Upstairs
                    for l in self.legs:  # raise legs
                        if l.direction == 0:
                            continue
                        l.raiseleg(100)

                    time.sleep(0.6) # 0.4 before

                    for l in self.legs:
                        l.step(False)
                        time.sleep(0.009)

                    time.sleep(1)
                elif key == "z":  # Reverse walking (more like dancing)
                    for l in self.legs:  # raise legs
                        if l.direction == 0:
                            continue
                        l.raiseleg(200)

                    if l.direction == 1:
                        for l in self.legs:
                            l.moveservo(l.servos[0], l.backwardangle, speed)
                        time.sleep(0.3)
                        for l in self.legs:
                            l.moveservo(l.servos[1], 485, speed)
                        time.sleep(0.3)
                        for l in self.legs:
                            l.moveservo(l.servos[2], 400, speed)

                        time.sleep(1)

                        l.direction = 0
                    elif l.direction == 0:
                        for l in self.legs:
                            l.moveservo(l.servos[0], l.forwardangle, speed)
                        time.sleep(0.3)
                        for l in self.legs:
                            l.moveservo(l.servos[1], 485, speed)
                        time.sleep(0.3)
                        for l in self.legs:
                            l.moveservo(l.servos[2], 400, speed)

                        time.sleep(1)

                        l.direction = 1

                    time.sleep(0.3)
                elif key == "l":  # Show load
                    self.showLoad()
                elif key == "u":  # Hybrid mode
                    self.hybrid()
                elif key == "o":  # Reset
                    self.reset()
                elif key == "p":  # Show positions
                    self.showPositions()
                elif key == "b":  # Battlestance
                    self.battlestance()
                elif key == "i":  # Dab
                    self.dab()
                elif key == '.':
                    break
            except:
                print "Exception in code:"
                traceback.print_exc(file=sys.stdout)
                print "Continuing..."
                continue

    # Reset function
    def reset(self):
        speed = 200

        print("Resetting..")

        for l in self.legs:
            l.moveservo(l.servos[0], 350, speed)

        time.sleep(0.3)

        for l in self.legs:
            l.moveservo(l.servos[2], 400, 200)

        time.sleep(0.3)

        for l in self.legs:
            l.moveservo(l.servos[1], 485, speed)

        print("Waiting 2 seconds before resetting tail!")

        time.sleep(2)

        print("Resetting tail")

        # Put Resetting Tail code here


        time.sleep(1)

        print("Done resetting!")

    # Battlestance
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

        # Change tail position
        l.moveservo(100, 800, speed)
        time.sleep(0.2)
        l.moveservo(101, 900, speed)
        time.sleep(0.2)
        l.moveservo(102, 1000, speed)
        time.sleep(0.2)
        l.moveservo(103, 500, speed)

        time.sleep(1)

    # Leg Retract
    def hybrid(self):
        speed = 100
        i = 0

        for l in self.legs:
            if i <= 2:
                l.moveservo(l.servos[0], 620, speed)
                l.moveservo(l.servos[1], 0, speed)
                l.moveservo(l.servos[2], 85, speed)
            else:
                l.moveservo(l.servos[0], 95, speed)
                l.moveservo(l.servos[1], 0, speed)
                l.moveservo(l.servos[2], 85, speed)

            i += 1

        time.sleep(1)
