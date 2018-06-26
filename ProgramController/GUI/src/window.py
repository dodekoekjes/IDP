#!/usr/bin/python3

import time
import sys
import threading
from input import Input
from controller import Controller
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QPushButton, QLabel

from .joystick import Joystick


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.font_btn = QFont()
        self.font_btn.setFamily("Arial")
        self.font_btn.setPointSize(12)
        self.init = False
        self.joy_display = []
        self.highstep = False

        #self.controller = None
        self.thread_controller = ThrControler(2, "Controller")
        self.thread_controller.start()
        print("thread1")
        self.read = threading.Thread(target=self.read_input)
        self.read.start()
        print("thread2")

        self.initUI()
        self.init = True

    def read_input(self):
        joystick_input = Input()
        MULTIPLIER = 1/511.5
        while True:
            output = joystick_input.read()

            x1 = int(output[0])
            y1 = int(output[1])
            b1 = bool(output[2])

            # joystick 2
            x2 = int(output[3])
            y2 = int(output[4])
            b2 = bool(output[5])
            x2_float = MULTIPLIER*x1-1
            y2_float = -(MULTIPLIER*y1-1)

            x1_float = MULTIPLIER*x2-1
            y1_float = -(MULTIPLIER*y2-1)
            if self.init:
                # self.joy_display[0].set_pos_inner(x1_float, y1_float)
                # self.joy_display[0].click = b1
                # self.joy_display[1].set_pos_inner(x2_float, y2_float)
                # self.joy_display[1].click = b2
                self.lbl_joy1.setText("Joy1:\t\tX: "+str(x1_float)[:5]+", Y: "+str(y1_float)[:5])
                # time.sleep(0.5)
                self.lbl_joy2.setText("Joy2:\t\tX: "+str(x2_float)[:5]+", Y: "+str(y2_float)[:5])
                time.sleep(0.5)

    def quit(self):
        print("Quitting...")
        QApplication.instance().quit()

    def toggle_legs(self):
        print("Toggling Legs...")
        self.thread_controller.update("manual")
    
    def step_height(self):
        print("Toggling Step height...")
        if not self.highstep:
            self.thread_controller.update("highstep")
            self.lbl_steps.setText("Steps:\t\tHIGH")
            self.highstep = True
        else:
            self.thread_controller.update("lowstep")
            self.lbl_steps.setText("Steps:\t\tLOW")
            self.highstep = False
    
    def dance(self):
        print("Dancing...")
        self.thread_controller.update("dance")
    
    def line_dance(self):
        print("Line Dancing...")
        self.thread_controller.update("linedance")

    def toggle_arm(self):
        print("Toggling Arm...")
        self.thread_controller.update("arm")

    def battlestance(self):
        print("Entering Battle Stance...")
        self.thread_controller.update("battlestance")

    def dab(self):
        print("Dabbing...")
        self.thread_controller.update("dab")

    def catchball(self):
        print("Catching Ball...")
        self.thread_controller.update("ball")

    def reset(self):
        print("Resetting")
        self.thread_controller.update("reset")

    def addButton(self, text, func, position=(8, 8), size=(80, 80)):
        button = QPushButton(text, self)
        button.setFont(self.font_btn)
        button.setGeometry(position[0], position[1], size[0], size[1])
        button.clicked.connect(func)

    def createButtons(self, resolution):
        self.addButton("X", func=self.quit, position=(resolution[0] - 38, 8), size=(30,30))
        self.addButton("Toggle\nLegs", func=self.toggle_legs)
        self.addButton("Toggle\nMovement", position=(96, 8), func=self.toggle_arm)
        self.addButton("Battle\nStance", position=(8, 96), func=self.battlestance)
        self.addButton("DAB", position=(96, 96), func=self.dab)
        self.addButton("Catch\nBall", position=(8, 88*2+8), func=self.catchball)
        self.addButton("Reset\nPositions", position=(96, 88*2+8), func=self.reset)
        self.addButton("Step\nHeight", position=(88*2+8, 88*2+8), func=self.step_height)
        self.addButton("Line\nDance", position=(88*3+8, 88*2+8), func=self.line_dance)
        self.addButton("D.A.N.C.E.", position=(88*4+8, 88*2+8), func=self.dance)

        self.lbl_controls = QLabel("Controls:\tMOVE", self)
        self.lbl_controls.move(88*2+8,8+16*0)

        self.lbl_movement = QLabel("Movement:\tLEGS", self)
        self.lbl_movement.move(88*2+8,8+16*1)

        self.lbl_steps = QLabel("Steps:\t\tLOW", self)
        self.lbl_steps.move(88*2+8,8+16*2)

        self.lbl_joy1 = QLabel("Joy1:\t\tX: 0.000, Y: 0.000", self)
        self.lbl_joy1.move(88*2+8,8*2+16*3)
        
        self.lbl_joy2 = QLabel("Joy2:\t\tX: 0.000, Y: 0.000", self)
        self.lbl_joy2.move(88*2+8,8*2+16*4)


    # def paintEvent(self, event):
    #     paint = QPainter()
    #     paint.begin(self)
    #     # optional
    #     paint.setRenderHint(QPainter.Antialiasing)
    #     # make a white drawing background
    #     paint.setBrush(Qt.white)
    #     paint.drawRect(event.rect())
    #     paint.setPen(Qt.black)

    #     col_clicked = QColor(50, 255, 50)
    #     col_normal  = QColor(210, 210, 210)
    #     # print(joy['pos_inner'])
    #     for joy in self.joy_display:
    #         paint.setBrush(Qt.gray)
    #         paint.drawEllipse(joy.center, joy.rad_outer[0], joy.rad_outer[1])
    #         paint.setBrush(Joystick.color_click if joy.click else Joystick.color)
    #         paint.drawEllipse(joy.pos_inner, joy.rad_inner[0], joy.rad_inner[1])
    #     paint.end()

    def initUI(self):
        screen_res = 480, 320   # Resolution of the pi's screen
        self.setGeometry(0, 0, screen_res[0], screen_res[1])
        self.setWindowTitle("Heinz Controller Interface - INATOR")
        
        # WINDOW CONTENT HERE

        self.createButtons(screen_res)

        # FINALIZING

        self.setWindowFlags(Qt.FramelessWindowHint)     
        # self.showMaximized()
        self.show()


class ThrControler(threading.Thread):
    def __init__(self, id, name):
        super().__init__()
        self.name = name
        self.id = id
        self.controller = Controller()

    def run(self):
        print("thread:", self.id, "name:", self.name, "created.")

    def update(self, stance):
        self.controller.stance = stance
        print("stance changed to:", stance, "check:", self.controller.stance)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())