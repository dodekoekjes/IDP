from movement import locomotion


def movement(numlegs=6, legjoints=3, numsteps=10):
    loco = locomotion.Locomotion(numlegs, legjoints)
    loco.printlegs()
    # loco.walk(numsteps)
    # loco.battlestance()
    # loco.dab()
    loco.manual()
    return "movement module has been executed"

def detection():
    return "detection module has been executed"

def somethingelse():
    pass
