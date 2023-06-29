from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

# Relay GPIO pins
relay1_pin = 16
relay2_pin = 20
relay3_pin = 21

factory = PiGPIOFactory(host='10.42.0.124')

relay1 = LED(relay1_pin, pin_factory=factory)
relay2 = LED(relay2_pin, pin_factory=factory)
relay3 = LED(relay3_pin, pin_factory=factory)
