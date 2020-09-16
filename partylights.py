#blinking lights
import time
import random
from adafruit_circuitplayground import cp
cp.pixels.brightness = .1
while True:
    mode = random.randint(1, 4)
    time.sleep (.5)
    if mode == 1:
        for i in range(1,random.randint(10,20)):
            cp.pixels.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            time.sleep (.2)
            cp.pixels.fill((0,0,0))
            time.sleep (.2)
    elif mode == 2: #dimming red lights
        for i in range (random.randint(3,6)):
            for j in range (255,-5,-5): 
                cp.pixels.fill((j, 0, 0))
        cp.pixels.fill((0,0,0))
    elif mode == 3:
        for i in range (1, random.randint(3,6) + 1 ):
            colors = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            for j in range (10): 
                cp.pixels[j] = colors
                time.sleep(.05)
            cp.pixels.fill ((0,0,0))
    elif mode == 4:
        for i in range (random.randint(5,10)):
            colorsa = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            for j in range (5):
                cp.pixels[j] = colorsa
            time.sleep(.2)
            for j in range (5):
                cp.pixels[j] = (0,0,0)

            colorsb = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            for j in range (5,10):
                cp.pixels[j] = colorsb
            time.sleep(.2)
            for j in range (5,10):
                cp.pixels[j] = (0,0,0)
