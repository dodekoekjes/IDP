from .leg import Leg
import time
import ax12

class Robot:

    def __init__(self, numlegs, legjoints):
        self.legs = [Leg(i, legjoints) for i in range(numlegs)]

    def printlegs(self):
        print([l.servos for l in self.legs])

    def walk(self, numsteps):
        for l in self.legs:
            l.reset()

        #l = self.legs[5]
        #for _ in range(numsteps):
        #    l.raiseleg()
        #    time.sleep(1)
        #    l.step()
        #    time.sleep(1)
        
        for _ in range(numsteps):
            for l in self.legs:
                if l.direction == 0:
                    continue
                l.raiseleg()
            time.sleep(1)
            for l in self.legs:
                l.step()
            time.sleep(3)
            
            for i in range(13):
                print (ax12.Ax12().readPosition(i+1))
            

        #for _ in range(numsteps):
        #    for l in self.legs:
        #        l.raiseleg()
        #        time.sleep(0.002)
        #    time.sleep(2)
        #    for l in self.legs:
        #        l.step()
        #        time.sleep(0.002)
        #    #time.sleep(0.5)
