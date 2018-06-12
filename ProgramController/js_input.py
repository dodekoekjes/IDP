#!/usr/bin/python3

import spidev
import os
import time
import RPi.GPIO as GPIO

# Define Axis Channels (channel 3 to 7 can be assigned for more buttons / joysticks)
vrx_channel1 = 0
vry_channel1 = 1
vrx_channel2 = 2
vry_channel2 = 3

# define button Channels
b_pin1 = 26
b_pin2 = 12

# define button status
b_pressed1 = False
b_pressed2 = False

# Time delay, which tells how many seconds the value is read out
delay = 0.5

# Rpi.GPIO init
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# setup button pins
GPIO.setup(b_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Spi init
spi = spidev.SpiDev()
spi.open(1, 2)
spi.max_speed_hz = 1350000


# Function for reading the MCP3008 channel between 0 and 7
def readChannel(channel):
    val = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    # print("raw data:", val, "\ndata:", data)
    return data


# endless loop
while True:

    # Determine position
    # Joystick 1
    vrx_pos1 = readChannel(vrx_channel1)
    vry_pos1 = readChannel(vry_channel1)

    # Joystick 2
    vrx_pos2 = readChannel(vrx_channel2)
    vry_pos2 = readChannel(vry_channel2)

    # Check button pressed
    # button 1
    if GPIO.input(b_pin1) == GPIO.HIGH and not b_pressed1:
        b_pressed1 = True
        print("Button 1 pressed\npin :", b_pin1)
    if GPIO.input(b_pin2) == GPIO.HIGH and not b_pressed2:
        b_pressed2 = True
        print("Button 2 pressed\npin :", b_pin2)

    if GPIO.input(b_pin1) == GPIO.LOW and b_pressed1:
        b_pressed1 = False
        print("Button 1 released\npin :", b_pin1)
    if GPIO.input(b_pin2) == GPIO.LOW and b_pressed2:
        b_pressed2 = False
        print("Button 2 released\npin :", b_pin2)
    # output


    # wait
    time.sleep(delay)
