from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

# LED GPIO pins
led_1_green_pin = 5
led_1_yellow_pin = 6
led_1_red_pin = 13

led_2_green_pin = 19
led_2_yellow_pin = 6
led_2_red_pin = 13

led_3_green_pin = 23
led_3_yellow_pin = 24
led_3_red_pin = 25

factory = PiGPIOFactory(host='10.0.0.7')

led_1_green = LED(led_1_green_pin, pin_factory=factory)
led_1_yellow = LED(led_1_yellow_pin, pin_factory=factory)
led_1_red = LED(led_1_red_pin, pin_factory=factory)

led_2_green = LED(led_2_green_pin, pin_factory=factory)
led_2_yellow = LED(led_2_yellow_pin, pin_factory=factory)
led_2_red = LED(led_2_red_pin, pin_factory=factory)

led_3_green = LED(led_3_green_pin, pin_factory=factory)
led_3_yellow = LED(led_3_yellow_pin, pin_factory=factory)
led_3_red = LED(led_3_red_pin, pin_factory=factory)
