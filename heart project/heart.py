import math
from turtle import *


speed(10000) # 
bgcolor('black')
color('#f73487') 

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

# Drawing the heart
penup()
for i in range(6000):
    # Calculate position
    x = hearta(i) * 20
    y = heartb(i) * 20
    
    # Draw line from center to the calculated point
    goto(0, 0)
    pendown()
    goto(x, y)
    penup()

done()
