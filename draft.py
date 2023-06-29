from gpiozero import Button, LED
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

trigger = Button(3)
resetbutton = Button(2)

switch_1_green = Button(17)
switch_1_yellow = Button(27)
switch_1_red = Button(22)

switch_2_green = Button(5)
switch_2_yellow = Button(6)
switch_2_red = Button(13)

switch_3_green = Button(23)
switch_3_yellow = Button(24)
switch_3_red = Button(25)

factory = PiGPIOFactory(host='10.42.0.124')

relay1 = LED(16, pin_factory=factory)
relay2 = LED(20, pin_factory=factory)
relay3 = LED(21, pin_factory=factory)

led_1_green = LED(17, pin_factory=factory)
led_1_yellow = LED(27, pin_factory=factory)
led_1_red = LED(22, pin_factory=factory)

led_2_green = LED(5, pin_factory=factory)
led_2_yellow = LED(6, pin_factory=factory)
led_2_red = LED(13, pin_factory=factory)

led_3_green = LED(23, pin_factory=factory)
led_3_yellow = LED(24, pin_factory=factory)
led_3_red = LED(25, pin_factory=factory)

led_1_green.source = switch_1_green
led_1_yellow.source = switch_1_yellow
led_1_red.source = switch_1_red

led_2_green.source = switch_2_green
led_2_yellow.source = switch_2_yellow
led_2_red.source = switch_2_red

led_3_green.source = switch_3_green
led_3_yellow.source = switch_3_yellow
led_3_red.source = switch_3_red

def relay_on():
    relay1.on()
    relay2.on()
    relay3.on()


def relay_off():
    relay1.off()
    relay2.off()
    relay3.off()

trigger.when_pressed = relay_on
resetbutton.when_pressed = relay_off


pause()
