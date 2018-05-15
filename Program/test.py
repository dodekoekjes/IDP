import pyax12
from pyax12.connection import Connection
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Connect to the serial port
serial_connection = Connection(port="/dev/ttyAMA18", rpi_gpio=True)

dynamixel_id = 1

# Print the control table of the specified Dynamixel unit
serial_connection.pretty_print_control_table(dynamixel_id)

# Close the serial connection
serial_connection.close()