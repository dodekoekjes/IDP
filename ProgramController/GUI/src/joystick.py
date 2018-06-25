from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPoint


class Joystick:
    color           = QColor(210, 210, 210)
    color_click     = QColor(50, 255, 50)

    def __init__(self, name, rad_outer, rad_inner, center, click):
        self.name           = name
        self.rad_outer      = rad_outer
        self.rad_inner      = rad_inner
        self.center         = center
        self.pos_inner      = center
        self.click          = click

    def set_pos_inner(self, xmult, ymult):
        self.pos_inner = QPoint(
            self.center.x() + xmult*20, 
            self.center.y() + ymult*20
        )
