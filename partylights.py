#blinking lights
import time
import random
from adafruit_circuitplayground import cp
cp.pixels.brightness = .1
while True:
    a = random.randint(1, 4)
    time.sleep (.5)
    print (a)
    if a == 1:
        repsa = random.randint(10,20)
        print (repsa)
    while a == 1: #flashing random colors
        cp.pixels.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        time.sleep (.2)
        cp.pixels.fill((0,0,0))
        time.sleep (.2)
        repsa -= 1
        print (repsa)
        if repsa == 0:
            a = random.randint(2,4)
            print(a)
    if a == 2: #dimming red lights
        repsb = random.randint(3,6)
        print (repsb)
    while a == 2:
        length = 1000
        j=0
        wait_down = .0
        while (j<length):
            cp.pixels.fill((255-j, 0, 0))
            j = j+5
            time.sleep(wait_down)
            if (j>255):
                j=0
                repsb -= 1
                print (repsb)
                if (repsb < 0): #failsafe in case 2 is picked twice in a row
                    repsb = 0
                    print ("uh oh")
                if repsb == 0:
                    j = 1001
                    cp.pixels.fill((0,0,0))
                    a = random.randint(1,4)
                    print (a)
    if a == 3:
        repsc = random.randint(3,6)
        print (repsc)
    while a == 3:
        colora = random.randint(0,255)
        colorb = random.randint(0,255)
        colorc = random.randint(0,255)
        cp.pixels[0] = (colora,colorb,colorc)
        time.sleep(.05)
        cp.pixels[1] = (colora,colorb,colorc)
        time.sleep (.05)
        cp.pixels[2] = (colora,colorb,colorc)
        time.sleep(.05)
        cp.pixels[3] = (colora,colorb,colorc)
        time.sleep (.05)
        cp.pixels[4] = (colora,colorb,colorc)
        time.sleep(.05)
        cp.pixels[5] = (colora,colorb,colorc)
        time.sleep (.05)
        cp.pixels[6] = (colora,colorb,colorc)
        time.sleep(.05)
        cp.pixels[7] = (colora,colorb,colorc)
        time.sleep (.05)
        cp.pixels[8] = (colora,colorb,colorc)
        time.sleep(.05)
        cp.pixels[9] = (colora,colorb,colorc)
        time.sleep (.05)
        cp.pixels.fill ((0,0,0))
        repsc -= 1
        print (repsc)
        if (repsc<0): #failsafe for if 3 is picked twice in a row
            repsc = 0
            print ("uh oh")
        if repsc == 0:
            a = random.randint(1, 4)
            print (a)
    if a == 4:
        repsd = random.randint(5,10)
        print (repsd)
    while a == 4: #half board flashing random colors
        colora = random.randint(0,255)
        colorb = random.randint(0,255)
        colorc = random.randint(0,255)
        coloraa = random.randint(0,255)
        colorbb = random.randint(0,255)
        colorcc = random.randint(0,255)
        cp.pixels[0] = (colora,colorb,colorc)
        cp.pixels[1] = (colora,colorb,colorc)
        cp.pixels[2] = (colora,colorb,colorc)
        cp.pixels[3] = (colora,colorb,colorc)
        cp.pixels[4] = (colora,colorb,colorc)
        time.sleep(.2)
        cp.pixels[0] = (0,0,0)
        cp.pixels[1] = (0,0,0)
        cp.pixels[2] = (0,0,0)
        cp.pixels[3] = (0,0,0)
        cp.pixels[4] = (0,0,0)
        cp.pixels[5] = (coloraa,colorbb,colorcc)
        cp.pixels[6] = (coloraa,colorbb,colorcc)
        cp.pixels[7] = (coloraa,colorbb,colorcc)
        cp.pixels[8] = (coloraa,colorbb,colorcc)
        cp.pixels[9] = (coloraa,colorbb,colorcc)
        time.sleep(.2)
        cp.pixels[5] = (0,0,0)
        cp.pixels[6] = (0,0,0)
        cp.pixels[7] = (0,0,0)
        cp.pixels[8] = (0,0,0)
        cp.pixels[9] = (0,0,0)
        repsd -= 1
        print (repsd)
        if (repsd<0):
            repsd = 0
            print ("uh oh")
        if repsd == 0:
            a = random.randint(1,4)
            print (a)