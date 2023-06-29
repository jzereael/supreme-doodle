from gpiozero import Button
import relay_control
import led_control

# Button GPIO pins
trigger_pin = 3
resetbutton_pin = 2

# Switch GPIO pins
switch_1_green_pin = 17
switch_1_yellow_pin = 27
switch_1_red_pin = 22

switch_2_green_pin = 5
switch_2_yellow_pin = 6
switch_2_red_pin = 13

switch_3_green_pin = 23
switch_3_yellow_pin = 24
switch_3_red_pin = 25

# Button objects
trigger = Button(trigger_pin)
resetbutton = Button(resetbutton_pin)

# Switch objects
switch_1_green = Button(switch_1_green_pin)
switch_1_yellow = Button(switch_1_yellow_pin)
switch_1_red = Button(switch_1_red_pin)

switch_2_green = Button(switch_2_green_pin)
switch_2_yellow = Button(switch_2_yellow_pin)
switch_2_red = Button(switch_2_red_pin)

switch_3_green = Button(switch_3_green_pin)
switch_3_yellow = Button(switch_3_yellow_pin)
switch_3_red = Button(switch_3_red_pin)

def setup_pins(pin_factory):
    global trigger, resetbutton, switch_1_green, switch_1_yellow, switch_1_red
    global switch_2_green, switch_2_yellow, switch_2_red, switch_3_green
    global switch_3_yellow, switch_3_red

    trigger.pin_factory = pin_factory
    resetbutton.pin_factory = pin_factory
    switch_1_green.pin_factory = pin_factory
    switch_1_yellow.pin_factory = pin_factory
    switch_1_red.pin_factory = pin_factory
    switch_2_green.pin_factory = pin_factory
    switch_2_yellow.pin_factory = pin_factory
    switch_2_red.pin_factory = pin_factory
    switch_3_green.pin_factory = pin_factory
    switch_3_yellow.pin_factory = pin_factory
    switch_3_red.pin_factory = pin_factory

def setup_sources():
    led_control.led_1_green.source = switch_1_green
    led_control.led_1_yellow.source = switch_1_yellow
    led_control.led_1_red.source = switch_1_red
    led_control.led_2_green.source = switch_2_green
    led_control.led_2_yellow.source = switch_2_yellow
    led_control.led_2_red.source = switch_2_red
    led_control.led_3_green.source = switch_3_green
    led_control.led_3_yellow.source = switch_3_yellow
    led_control.led_3_red.source = switch_3_red

def relay_on():
    relay_control.relay1.on()
    relay_control.relay2.on()
    relay_control.relay3.on()

def relay_off():
    relay_control.relay1.off()
    relay_control.relay2.off()
    relay_control.relay3.off()
