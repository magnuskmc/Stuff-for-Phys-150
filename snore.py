import board
import digitalio
import time

# set up the (red) LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    for brightness in [1.0, 0.8, 0.6, 0.4, 0.2, 0.0, 0.2, 0.4, 0.6, 0.8]:
        # brightness is measured out of a max of 1.0
        T_fast = 0.005
        T_on = brightness*T_fast
        T_off = (1-brightness)*T_fast
        num_repeats=100
        i=0
        while (i<num_repeats):
            led.value = True
            time.sleep(T_on)
            led.value = False
            time.sleep(T_off)
            i=i+1