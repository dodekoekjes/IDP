#!/usr/bin/python3

import threading
import time
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QPoint, QThread

from .window import Window


class ControllerApp(QThread):
    instance = None

    def __init__(self):

        super().__init__()
        if not ControllerApp.instance:
            ControllerApp.instance = Window()

    def run(self):
        print("is printed")

    def __del__(self):
        self.wait(2)
    @staticmethod
    def delete():
        ControllerApp.instance = None


def tr1():
    a = 88*3+48
    time.sleep(1)
    print("Loop starting...")

    xmult = 0.0
    ymult = 0.0

    for _ in range(50):
        # Break and end thread when instance is deleted
        if not ControllerApp.instance:
            break

        # print(Test.instance)
        # a += 1

        xmult += 0.015
        ymult += 0.015

        ControllerApp.instance.joy_display[1].set_pos_inner(xmult, ymult)
        ControllerApp.instance.repaint()
        time.sleep(0.08)
    
    print("Quitting Loop thread...")


def update(x1, y1, b1, x2, y2, b2):
    print("test")


# t1 = threading.Thread(target=tr1)
# t1.start()
#
# app = QApplication(sys.argv)
# ex = ControllerApp()
# app.exec_()
# ControllerApp.delete()
#
# t1.join()
# print("Quitting Main thread...")