#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
from simple_pid import PID

GPIO.cleanup() 


pid = PID(.1,0.5, 0.05, setpoint = 90)
pid.sample_time = 0.1


pid.output_limits = (0,100)

led_pin = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
led = GPIO.PWM(led_pin, 500)
led.start(100)
time.sleep(2)


#define the pin that goes to the circuit
pin_to_circuit = 7

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

pid.set_auto_mode(True, last_output=80)
#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        value = rc_time(pin_to_circuit)
        led_brightness = map_value(value,100 , 60000, 100, 0)
        output = pid(led_brightness)
        print(f"pid output = {output}, \t led_brightness = {led_brightness}\n")
        led.ChangeDutyCycle(output)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
