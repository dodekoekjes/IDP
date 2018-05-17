from pyax12.connection import Connection
# import RPi.GPIO as gpio
from ax12 import Ax12


class MovementControls:
    """Manages movement controls"""
    def __init__(self):
        """Init"""
        print("class: MovementControls created.")
        ax = Ax12()
        ax.

    def test(self):
        # gpio.setup(18, gpio.OUT)
        # gpio.setwarnings(False)
        serial_connection = Connection(port="/dev/ttyAMA0", rpi_gpio=True)

        dynamix_id = 3

        is_available = serial_connection.ping(dynamix_id)

        print(is_available)

        serial_connection.close()


class ArmControls:
    """Manages arm controls"""
    def __init__(self):
        """Init"""
        print("class: ArmControls created.")
