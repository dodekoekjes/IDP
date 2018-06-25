#!/usr/bin/python3

## Divide 1 by half the maximum possible value
MULTIPLIER = 1/511.5

## Sample joystick x position
joyval_x = 0

## Multiply afformentioned position by the MULTIPLIER and subtract 1
joyval_float = MULTIPLIER*joyval_x-1
print(joyval_float)