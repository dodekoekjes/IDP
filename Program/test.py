from time import sleep
import ax12

servos = ax12.Ax12()

anglePosition = 500

motorSpeed = 200

#servos.learnServos(1, 254)

servoid = 42

def move(id, anglePos, speed):
    servos.moveSpeedRW(id, anglePos, speed)
    sleep(0.02)
    servos.action()
    sleep(2)

while(1):
    move(12, 1000, 200)
    move(12, 0, 200)
    #move(42, 1000, 1023)
