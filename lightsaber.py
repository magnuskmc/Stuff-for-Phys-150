from adafruit_circuitplayground import cp
from adafruit_circuitplayground.express import cpx
import time
import math
import random
read_delay = 0.01
g=9.801
a_floor = 1
x, y, z = cpx.acceleration
a0 = math.sqrt(x*x+y*y+z*z)/g
t0 = time.monotonic()
x, y, z = cpx.acceleration
a1 = math.sqrt(x*x+y*y+z*z)/g
t1 = time.monotonic()
while True:
    if cp.button_a:
        cp.pixels.fill((25,25,250))
        cp.play_file("ignite.wav")
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
                randswing = random.randint(1,4)
                if randswing == 1:
                    cp.play_file("Swing01.wav")
                elif randswing == 2:
                    cp.play_file("Swing02.wav")
                elif randswing == 3:
                    cp.play_file("Swing03.wav")
                elif randswing == 4:
                    cp.play_file("Swing04.wav")
            elif cp.button_b:
                cp.pixels.fill((0,0,0))
                cp.play_file("turn_off.wav")
                break
            else:
                randhum = random.randint(1,3)
                if randhum == 1:
                    cp.play_file("Hum1.wav")
                if randhum == 2:
                    cp.play_file("Hum 2.wav")
                if randhum == 3:
                    cp.play_file("Hum 3.wav")
            a0=a1
            a1=a2
            t0=t1
            t1=t2
            time.sleep(read_delay)
