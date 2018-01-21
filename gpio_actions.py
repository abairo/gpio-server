import OPi.GPIO as GPIO
import json

## SET GPIO MODE
# GPIO.setmode(GPIO.BOARD)
## CONFIG GPIOS PINS
# GPIO.setup(GATE_1, GPIO.OUT)

def get_status(gpio_pin:int):
    return GPIO.input(gpio_pin)


def toggle_status(gpio_pin:int):
    GPIO.output(gpio_pin, not get_status(gpio_pin))
    return True


def open_gate(gate:int):
    GPIO.output(gate, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(gate, GPIO.LOW)
    return True
 

def to_dictionary(obj):
    if obj:
        return json.loads(obj)
    else:
        return None


def gpio_handler(msg):
    msg_dict = to_dictionary(msg)
    pin = msg_dict['pin']

    if pin == GATE_1:
        return open_gate(pin)        
    else:
        return toggle_status(pin)
