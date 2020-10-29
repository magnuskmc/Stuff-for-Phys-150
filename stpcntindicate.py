
import time
import math
from adafruit_circuitplayground.express import cpx
from adafruit_circuitplayground import cp
step_goal = 10000
cp.pixels.brightness = 0.05


num_steps = 0

read_delay = 0.2

g=9.801
a_floor = 1.2

x, y, z = cpx.acceleration
a0 = math.sqrt(x*x+y*y+z*z)/g
t0 = time.monotonic()

x, y, z = cpx.acceleration
a1 = math.sqrt(x*x+y*y+z*z)/g
t1 = time.monotonic()

while True:

    x, y, z = cpx.acceleration
    a2 = math.sqrt(x*x+y*y+z*z)/g
    t2 = time.monotonic()

    slope1 = (a1-a0)/(t1-t0)
    slope2 = (a2-a1)/(t2-t1)
    if(
        slope1>0 and slope2<0
        and a1 > a_floor
        ):

        num_steps += 1
        step_percent = num_steps/step_goal
        print(step_percent)
        print(num_steps)
        if step_percent >= .1 and step_percent < .19 :
            cp.pixels[9]=(50,0,0)
        elif step_percent >= .2 and step_percent < .29 :
            for i in range(8,9):
                cp.pixels[i]= (50,0,0)
        elif step_percent >= .3 and step_percent < .39 :
            for i in range(7,9):
                cp.pixels[i]= (50,0,0)
        elif step_percent >= .4 and step_percent < .49 :
            cp.pixels[6]=(25,25,0)
            for i in range(7,9):
                cp.pixels[i]= (50,0,0)
        elif step_percent >= .5 and step_percent < .59 :
            for j in range(5,6):
                cp.pixels[j]=(25,25,0)
            for i in range(7,9):
                cp.pixels[i]= (50,0,0)
        elif step_percent >= .6 and step_percent < .69 :
            for j in range(4,6):
                cp.pixels[j]=(25,25,0)
            for i in range(7,9):
                cp.pixels[i]= (50,0,0)
        elif step_percent >= .7 and step_percent < .79 :
            for j in range(3,6):
                cp.pixels[j]=(25,25,0)
            for i in range(7,9):
                cp.pixels[i]= (50,0,0)
        elif step_percent >= .8 and step_percent < .89 :
            cp.pixels[2]=(0,50,0)
            for j in range(3,6):
                cp.pixels[j]=(25,25,0)
            for i in range(7,9):
                cp.pixels[i]= (50,0,0)
        elif step_percent >= .9 and step_percent < .99 :
            cp.pixels[2]=(0,50,0)
            cp.pixels[1]=(0,50,0)
            for j in range(3,6):
                cp.pixels[j]=(25,25,0)
            for i in range(7,9):
                cp.pixels[i]= (50,0,0)
        elif step_percent == 1 :
            for i in range(3):
                cp.pixels.fill((0,50,0))
                time.sleep (.2)
                cp.pixels.fill((0,0,0))
                time.sleep (.2)
            cp.pixels.fill((0,0,50))
    a0=a1
    a1=a2
    t0=t1
    t1=t2

    time.sleep(read_delay)

