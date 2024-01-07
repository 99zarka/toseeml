import RPi.GPIO as GPIO


# Set up GPIO pins
joystick_button_pin = 31
joystick_y_pin = 33
joystick_x_pin = 35
joystick_high_volt_pin = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(joystick_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(joystick_y_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(joystick_x_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(joystick_high_volt_pin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.output(joystick_high_volt_pin, GPIO.HIGH)

# Read joystick input
def get_joystick_state():
    x_value = GPIO.input(joystick_x_pin)
    y_value = GPIO.input(joystick_y_pin)
    button_value = GPIO.input(joystick_button_pin)
    
    state=""
    
    if not button_value:
        state="pressed"
    elif not x_value and not y_value:
        state="back and down"
    elif not x_value:
        state="back"
    elif not y_value:
        state="down"
    return state