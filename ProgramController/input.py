import spidev
import os
import printinput
import RPi.GPIO as GPIO


class Input():
    def __init__(self):
        """Initialize SPI channels"""
        # Define Axis Channels (channel 3 to 7 can be assigned for more buttons / joysticks)
        self.vrx_channel1 = 0
        self.vry_channel1 = 1
        self.vrx_channel2 = 2
        self.vry_channel2 = 3

        # define button Channels
        self.b_pin1 = 26
        self.b_pin2 = 12

        self.b_pressed1 = False
        self.b_pressed2 = False

        # Time delay, which tells how many seconds the value is read out
        self.delay = 0.5

        # RPi.GPIO init
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # setup button pins
        GPIO.setup(self.b_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.b_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.spi = spidev.SpiDev()
        self.spi.open(1, 2)
        self.spi.max_speed_hz = 1350000

        # dev
        self.vrx_pos1 = "[PLACEHOLDER]"
        self.vry_pos1 = "[PLACEHOLDER]"
        self.vrx_pos2 = "[PLACEHOLDER]"
        self.vry_pos2 = "[PLACEHOLDER]"

    def read_channel(self, channel):
        val = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((val[1] & 3) << 8) + val[2]
        # print("raw data:", val, "\ndata:", data)
        return data

    def read(self, args=None):
        """Returns nputs"""
        values = [self.vrx_pos1, self.vry_pos1, self.b_pressed1, self.vrx_pos2, self.vry_pos2, self.b_pressed2]
        printinput.PrintInput(3, "print", self.vrx_pos1, self.vry_pos1, self.b_pressed1, self.vrx_pos2, self.vry_pos2, self.b_pressed2, 0.5).start()
        if args == "dev":
            return values
        else:
            # Determine position
            # Joystick 1
            self.vrx_pos1 = self.read_channel(self.vrx_channel1)
            self.vry_pos1 = self.read_channel(self.vry_channel1)

            # Joystick 2
            self.vrx_pos2 = self.read_channel(self.vrx_channel2)
            self.vry_pos2 = self.read_channel(self.vry_channel2)

            # Check button pressed
            # button 1
            if GPIO.input(self.b_pin1) == GPIO.HIGH and not self.b_pressed1:
                self.b_pressed1 = True
                print("Button 1 pressed\npin :", self.b_pin1)
            if GPIO.input(self.b_pin2) == GPIO.HIGH and not self.b_pressed2:
                self.b_pressed2 = True
                print("Button 2 pressed\npin :", self.b_pin2)

            if GPIO.input(self.b_pin1) == GPIO.LOW and self.b_pressed1:
                self.b_pressed1 = False
                print("Button 1 released\npin :", self.b_pin1)
            if GPIO.input(self.b_pin2) == GPIO.LOW and self.b_pressed2:
                self.b_pressed2 = False
                print("Button 2 released\npin :", self.b_pin2)
            # output
            printinput.PrintInput(3, "print", self.vrx_pos1, self.vry_pos1, self.b_pressed1, self.vrx_pos2, self.vry_pos2, self.b_pressed2, 0.5).start()
            return values
