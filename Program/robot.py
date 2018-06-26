from leg import Leg
import time
import ax12
import sys, traceback
import RPi.GPIO as GPIO


class Robot:

    def __init__(self, numlegs, legjoints):
        self.legs = [Leg(i, legjoints) for i in range(numlegs)]
        self.direction = numlegs % 2
        self.raisepos = 200

        # GPIO.setmode(GPIO.BCM)

    def printlegs(self):
        print([l.servos for l in self.legs])

    # Dab
    def dab(self):
        speed = 200
        leg3, leg4 = self.legs[2], self.legs[3]
        i = 0

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
    def manual(self, x=0, y=0):
        print("manual executed with x:", x,"and y:",y)
        mv_delta = 30
        yspeed = 200 * abs(y)
        speed = 200
        s1 = 350
        s2 = 400  # 150
        s3 = 400  # 150

        print("HEINZ: Manual mode activated")

        try:
            if y > 0: # Walking
                for l in self.legs:  # raise legs
                    if l.direction == 0:
                        continue
                    l.raiseleg(self.raisepos)

                time.sleep(0.4)
                for l in self.legs:  # walking
                    l.step(False)
                    time.sleep(0.009)
                time.sleep(1)
            elif y < 0 : # Reverse walking
                for l in self.legs:  # raise legs
                    if l.direction == 0:
                        continue
                    l.raiseleg(self.raisepos)

                time.sleep(0.4)
                for l in self.legs:  # walking
                    l.step(True)
                    time.sleep(0.009)
                time.sleep(1)
            elif x > 0:
                for l in self.legs:
                    if l.direction == 0:
                        continue
                    l.raiseleg(200)

                time.sleep(0.4)
                for l in self.legs:
                    l.step(False, 2)
                    time.sleep(0.009)
                time.sleep(1)
            elif x < 0:
                for l in self.legs:
                    if l.direction == 0:
                        continue
                    l.raiseleg(200)

                time.sleep(0.4)

                for l in self.legs:
                    l.step(False, 1)
                    time.sleep(0.009)
                time.sleep(1)

        except:
            print("Exception in code:")
            traceback.print_exc(file=sys.stdout)
            print("Continuing...")

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

        time.sleep(1)

        print("Done resetting!")

    # Battlestance
    def battlestance(self):
        speed = 150

        # # Reset
        # for l in self.legs:
        #     l.reset()
        # time.sleep(1)

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

        # # Change tail position
        # l.moveservo(100, 800, speed)
        # time.sleep(0.2)
        # l.moveservo(101, 900, speed)
        # time.sleep(0.2)
        # l.moveservo(102, 1000, speed)
        # time.sleep(0.2)
        # l.moveservo(103, 500, speed)

        # time.sleep(1)

    # Go Upstairs
    def toggleStairs(self):
        if self.raisepos == 200:
            self.raisepos = 400
        elif self.raisepos == 400:
            self.raisepos = 200


    # Leg Retract
    def drive(self, drive_mode, x=0, y=0):
        if not drive_mode:
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
        else:
            print("let the robot drive\n X:", x, "Y:", y)
        try:
            PIN_PWM_R = 16 #36
            PIN_FORWARD_R = 21 #40
            PIN_BACKWARD_R = 20 #38

            PIN_PWM_L = 13 #33
            PIN_BACKWARD_L = 19 #35
            PIN_FORWARD_L = 26 #37
            SPEED =  100

            GPIO.setup(PIN_PWM_R, GPIO.OUT)
            GPIO.setup(PIN_FORWARD_R, GPIO.OUT)
            GPIO.setup(PIN_BACKWARD_R, GPIO.OUT)

            GPIO.setup(PIN_PWM_L, GPIO.OUT)
            GPIO.setup(PIN_FORWARD_L, GPIO.OUT)
            GPIO.setup(PIN_BACKWARD_L, GPIO.OUT)

            pwmR=GPIO.PWM(PIN_PWM_R, 100)
            pwmL=GPIO.PWM(PIN_PWM_L, 100)
            pwmR.start(0)
            pwmL.start(0)
            
            if x == 0 and y > 0.5:
                GPIO.output(PIN_FORWARD_R, True)
                GPIO.output(PIN_BACKWARD_R, False)
                GPIO.output(PIN_FORWARD_L, True)
                GPIO.output(PIN_BACKWARD_L, False)
            elif x == 0 and y < -0.5:
                GPIO.output(PIN_FORWARD_R, False)
                GPIO.output(PIN_BACKWARD_R, True)
                GPIO.output(PIN_FORWARD_L, False)
                GPIO.output(PIN_BACKWARD_L, True)
            elif x > 0.5 and y == 0:
                GPIO.output(PIN_FORWARD_R, False)
                GPIO.output(PIN_BACKWARD_R, True)
                GPIO.output(PIN_FORWARD_L, True)
                GPIO.output(PIN_BACKWARD_L, False)
            elif x < -0.5 and y == 0:
                GPIO.output(PIN_FORWARD_R, True)
                GPIO.output(PIN_BACKWARD_R, False)
                GPIO.output(PIN_FORWARD_L, False)
                GPIO.output(PIN_BACKWARD_L, True)
            
            pwmR.ChangeDutyCycle(SPEED)
            pwmL.ChangeDutyCycle(SPEED)
            GPIO.output(PIN_PWM_R, True)
            GPIO.output(PIN_PWM_L, True)

            if x == 0 and y == 0:
                GPIO.output(PIN_PWM_R, False)
                GPIO.output(PIN_PWM_L, False)

                GPIO.output(PIN_BACKWARD_R, False)
                GPIO.output(PIN_FORWARD_R, False)
                GPIO.output(PIN_BACKWARD_L, False)
                GPIO.output(PIN_FORWARD_L, False)
            
            pwmR.stop()
            pwmL.stop()
        except:
            traceback.print_exc(file=sys.stdout)




    def dance(self):
        print("let the robot dance")