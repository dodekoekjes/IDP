import math

right1 = True
left1 = False
forward1 = False
backward1 = True

x1 = 1000
y1 = 400

#print(math.pow(50, 2))
speed1 = 0
if right1 and forward1:
    try:
        speed1 = math.sqrt(math.pow((x1 - 600), 2) + math.pow((y1 - 600), 2))
    except:
        speed1 = 0
elif right1 and backward1:
    try:
        speed1 = math.sqrt(math.pow((x1 - 600), 2) + math.pow((400 - y1), 2))
    except:
        speed1 = 0
elif left1 and forward1:
    try:
        speed1 = math.sqrt(math.pow((400 - x1), 2) + math.pow((y1 - 600), 2))
    except:
        speed1 = 0
elif left1 and backward1:
    try:
        speed1 = math.sqrt(math.pow((400 - x1), 2) + math.pow((400 - y1), 2))
    except:
        speed1 = 0

print("speed:", speed1)

print(50*100/400)
