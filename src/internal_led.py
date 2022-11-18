from machine import Pin
import utime

led = Pin(28, Pin.OUT)
delay = .4

while True:
    led.value(1)
    utime.sleep(delay)
    led.value(0)
    utime.sleep(delay)
