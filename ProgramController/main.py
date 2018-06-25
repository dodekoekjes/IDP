#!/usr/bin/python3
from GUI.src import application
from controller import Controller
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QPoint, QThread
import sys


class Main:
    def __init__(self):
        app = QApplication(sys.argv)
        ex = application.ControllerApp()
        app.exec_()
        ex.delete()
        print("Quitting Main thread...")


if __name__ == '__main__':
    Main()