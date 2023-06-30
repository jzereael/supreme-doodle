from gpiozero import Button, LED
from signal import pause
from threading import Timer

trigger = Button(2)

relay = LED(19)

SW_R = Button(16)
SW_G = Button(20)
SW_Y = Button(21)

R = LED(17)
G = LED(27)
B = LED(22)

def relay_on(RGB, last):
    relay.on()
    if last.is_active:
        last.off()
    last = RGB
    RGB.on()
    #   start timer
    timer = Timer(5, relay_off, args=())
    timer.start()

def relay_off():
    print("Off")
    relay.off()

def apply_source(SWITCH_INPUT, LED_OUTPUT):
    LED_OUTPUT.source = SWITCH_INPUT

def led_on(L1):
    print("led_on")
    L1.on()

def x(RGB):
    RGB=R
    print("Button 5 pressed",RGB.pin)

def y(RGB):
    RGB=G
    print("Button 6 pressed",RGB.pin)

def z(RGB):
    RGB=B
    print("Button 13 pressed",RGB.pin)

def setup():
    SW_R.when_pressed = x
    SW_G.when_pressed = y
    SW_Y.when_pressed = z
    
    if (SW_R.value):
        RGB=R
        return RGB
    if (SW_G.value):
        RGB=G
        return RGB
    if (SW_Y.value):
        RGB=B
        return RGB


def run(x_1,last):
        if trigger.is_pressed :
                print("Triggering ON:",RGB)
                print("Current RGB:",RGB)
                print("Current x_1:", x_1)
                print("Current last:", last)
                relay_on(x_1, last)


x_1 = None
last = None
while True:
    RGB = setup()
    if last is None:
        last = RGB
    if RGB is not None:
        x_1 = RGB
    run(x_1, last)
    
#trigger.when_pressed = relay_on(RGB)

resetbutton = Button(3)
resetbutton.when_pressed = relay_off


pause()