import sys, traceback

from .robot import Robot


def main():
    bot = Robot(numlegs=6, legjoints=3)
    bot.printlegs()
    bot.walk(numsteps=100)

main()
