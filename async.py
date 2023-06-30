from gpiozero import Button, LED
from signal import pause
from threading import Timer

relay = LED(19)

SW_R = Button(16)
SW_G = Button(20)
SW_Y = Button(21)
RGB =''
R = LED(17)
G = LED(27)
B = LED(22)

def relay_on(RGB):
    print("On")
    relay.on()
    RGB[0].on()
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

def x():
    print("Button 5 pressed")
    R.on()
    RGB=R,Button(16)

def y():
    print("Button 6 pressed")
    G.on()
    RGB=G,Button(20)

def z():
    print("Button 13 pressed")
    B.on
    RGB=B,Button(21)

SW_R.when_pressed = x
SW_G.when_pressed = y
SW_Y.when_pressed = z

trigger = Button(2)
trigger.when_pressed = relay_on(RGB)

resetbutton = Button(3)
resetbutton.when_pressed = relay_off


pause()