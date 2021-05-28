import RPi.GPIO as GPIO
from time import sleep

lights = {
    'one': 18, 
    'two': 14, 
    'three': 15, 
    'four': 23 
}

GPIO.setwarnings(False)

# Set pins as numbers
GPIO.setmode(GPIO.BCM)

# Setup pins 
for pin in lights.values(): 
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


def lights_on():
    for pin in lights.values(): 
        GPIO.output(pin, GPIO.HIGH)
        sleep(1)

def lights_off(): 
    for pin in lights.values(): 
        GPIO.output(pin, GPIO.LOW)
        sleep(1)




