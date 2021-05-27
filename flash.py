from gpiozero import LED
from time import sleep

lights = [{
    'one': 18, 
    'two': 14, 
    'three': 15, 
    'four': 23 
}]

def lights_on(lights): 
    for light in lights.values(): 
        LED(light).on()
        sleep(1)

def lights_off(lights): 
    for light in lights.values(): 
        LED(light).off()
        sleep(1)
