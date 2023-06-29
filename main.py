from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause
import gpio_control
import time, threading


factory = PiGPIOFactory(host='10.0.0.7')

gpio_control.setup_pins(factory)
gpio_control.setup_sources()

gpio_control.trigger.when_pressed = gpio_control.relay_on
gpio_control.resetbutton.when_pressed = gpio_control.relay_off

if __name__ == '__main__':
    pause()
    foo()