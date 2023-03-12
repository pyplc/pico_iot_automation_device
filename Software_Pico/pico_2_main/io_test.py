from machine import Pin
import time

led = Pin(0, Pin.OUT)
led25 = led = Pin(25, Pin.OUT, Pin.PULL_DOWN)

while True:
    led.value(1)
    led25.on()
    time.sleep(1)
    led.value(0)
    led25.off()
    time.sleep(1)
