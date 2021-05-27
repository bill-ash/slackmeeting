from gpiozero import LED
from time import sleep

led1 = LED(18)
led2 = LED(14)
led3 = LED(15)
led4 = LED(23)

while True:
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    sleep(1)
    led1.off()
    sleep(1)
