from object_detection import ObjectDetection
from controls import ArmControls
from builder import Builder
from dancing import Dancing
from controls import MovementControls
from sound_recognition import SoundRecognition


class Controller:
    """This class manages all the modules"""
    def __init__(self):
        """Creates all the modules"""
        print("class: Controller created.")
        self.arm = ArmControls()
        self.builder = Builder()
        self.dancing = Dancing()
        self.direction = ObjectDetection()
        self.movement = MovementControls()
        self.sound = SoundRecognition()

    def update(self):
        """Updates the modules"""
        print("Update executed")
