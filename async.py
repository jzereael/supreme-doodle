from gpiozero import Button, LED
from signal import pause
from threading import Timer

relay = LED(19)

def hello():
    print("On")
    relay.on()
    #   start timer
    timer = Timer(5, relay_off, args=())
    timer.start()

def relay_off():
    print("Off")
    relay.off()

button_on = Button(2)
button_on.when_pressed = hello


button_off = Button(3)
button_off.when_pressed = relay_off


pause()