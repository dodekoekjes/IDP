import time
import RPi.GPIO as GPIO


class Leds:

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(25, GPIO.OUT )
    GPIO.setup(8, GPIO.OUT )
    GPIO.setup(7, GPIO.OUT )

    def vumeter (self):
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)

        GPIO.cleanup()

    def flowing(self):
        GPIO.output(25, GPIO.LOW)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)

        GPIO.cleanup()

    def disco(self):
        GPIO.output(25, GPIO.LOW)
        GPIO.output(8, GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)

        GPIO.cleanup()

    def rgb(self):
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)

        GPIO.cleanup()

    def breath(self):
        GPIO.output(25, GPIO.LOW)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)

        GPIO.cleanup()

    def lazer(self):
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)

        GPIO.cleanup()

    def breath(self):
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)

        GPIO.cleanup()


