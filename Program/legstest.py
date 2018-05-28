from time import sleep
import ax12
import RPi.GPIO as GPIO

import sys

from random import randint

servos = ax12.Ax12()
#print servos.readPosition(1)
#print servos.readPosition(2)
#print servos.readPosition(3)
#print servos.learnServos(1, 254)
#while True:
#    a = randint(300, 800)
#    servos.moveSpeed(42, a, 200)
#    sleep(2)

#servos.moveSpeedRW(7, 200, 200)
#sleep(0.02)
#servos.action()
#sleep(2)

#servos.setID(13, 6)
#servos.setID(14, 6)

yMinLimit = 200
yMaxLimit = 900

xMinLimit = 70
xMaxLimit = 500

a = 0

def rust():
    servos.moveSpeed(1, 350, 200)
    servos.moveSpeed(2, 0, 200)
    servos.moveSpeed(3, 70, 200)

def moveLeg():
    #if servos.readPosition(1) >= xMinLimit:
    #reset()
    moveX(1, xMaxLimit, 200)

intersleep = 0.5
def reset_all():
    numlegs = 4
    
    
    for i in range(4):
        
        servos.moveSpeed(i * 3 + 2, 150, 200)
        servos.moveSpeed(i * 3 + 3, 150, 200)
        servos.moveSpeed(i * 3 + 1, 350, 200)
        sleep(0.5)
    
    #servos.moveSpeed(2, 300, 200)
    #servos.moveSpeed(3, 300, 200)
    #servos.moveSpeed(1, 350, 200)
    
    wait = 3
    for i in range(wait):
        print(str(wait - i) + "...")
        sleep(1)

reset_all()
intersleep = 1

orig_stdout = sys.stdout
sys.stdout = open('log', 'w')
do_loop = True
while(do_loop):
    #servos.readLoad(3)
    #servos.readLoad(6)
    #servos.readLoad(9)
    #servos.readLoad(12)
    
    
    if a == 0:
        #servos.moveSpeed(1, 500, 200)
        #servos.moveSpeed(2, 500, 200)
        #servos.moveSpeed(3, 500, 200)
        
        for i in range(4):
            #servos.moveSpeed(i * 3 + 1, 400, 200)
            servos.moveSpeed(i * 3 + 2, 500, 200)
            servos.moveSpeed(i * 3 + 3, 500, 200)
            
            print(str(i*3+1) + ": " + str(servos.readLoad(i*3+1)))
            print(str(i*3+2) + ": " + str(servos.readLoad(i*3+2)))
            print(str(i*3+3) + ": " + str(servos.readLoad(i*3+3)))
        
        #sleep(intersleep)
        a+=1
    else:
        #servos.moveSpeed(1, xMaxLimit, 200)
        #sleep(0.5)
        #servos.moveSpeed(2, yMaxLimit, 200)
        #sleep(0.25)
        # OMHOOG
        #servos.moveSpeed(11, 0, 200)
        #servos.moveSpeed(8, 0, 200)
        #servos.moveSpeed(5, 0, 200)
        #servos.moveSpeed(2, 0, 200)
        
        #servos.moveSpeed(1, 350, 200)
        #servos.moveSpeed(2, 150, 200)
        #servos.moveSpeed(3, 150, 200)
        
        for i in range(4):
            #servos.moveSpeed(i * 3 + 1, 350, 100)
            servos.moveSpeed(i * 3 + 2, 150, 200)
            servos.moveSpeed(i * 3 + 3, 150, 200)
            
            print(str(i*3+1) + ": " + str(servos.readLoad(i*3+1)))
            print(str(i*3+2) + ": " + str(servos.readLoad(i*3+2)))
            print(str(i*3+3) + ": " + str(servos.readLoad(i*3+3)))
            
        #sleep(intersleep)
        #sleep(intersleep)
        #sleep(intersleep)

        #sleep(intersleep)
        a=0
    
    sleep(1.5)

sys.stdout = orig_stdout
print("Goodbye :c")


        
#moveLeg()

    #a = randint(58, 511)
    #servos.moveSpeed(1, a, 200)
    #moveLeg()
    #print servos.readPosition(14)
    #move(6, 0, 200)
