from gpiozero import Button, LED
from signal import pause
from threading import Timer

relay = LED(19)

SW_R = Button(5)
SW_G = Button(6)
SW_Y = Button(13)

R = LED(17)
G = LED(27)
B = LED(22)

def relay_on():
    print("On")
    relay.on()
   # apply_source(SW_R,R)

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
def y():
    print("Button 6 pressed")
def z():
    print("Button 13 pressed")


SW_R.when_pressed = x
SW_G.when_pressed = y
SW_Y.when_pressed = z

trigger = Button(2)
trigger.when_pressed = relay_on

resetbutton = Button(3)
resetbutton.when_pressed = relay_off


pause()