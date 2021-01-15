#imports
from gpiozero import Servo
from gpiozero import Button
import time

"""
Team 37
Servo Control
"""

servoPin1 = 17
servoPin2 = 18
button1_pin = 4
button2_pin = 21
button1 = Button(button1_pin)
button2 = Button(button2_pin)

motor1 = Servo(servoPin1, max_pulse_width = 2.7e-3, min_pulse_width = 5e-4)
motor2 = Servo(servoPin2, max_pulse_width = 2.7e-3, min_pulse_width = 5e-4)

init_val = -1 #resetting motor
motor1.value = init_val
motor2.value = init_val
try:
    while True:
       # if button1.is_pressed and motor1.value != 1:
           motor1.value += 0.1
           motor2.value += 0.1
           time.sleep(0.05)
           print("Button 1 is Pressed")
           if motor1.value and motor2.value == 1:
               print("Motor has exceeded max range")
               print("To turn back, press the other button")

        elif button2.is_pressed and motor2.value != -1:
            motor1.value -= 0.05
            motor2.value -= 0.05
            time.sleep(0.05)
            print("Button 2 is pressed")

            if motor1.value and motor2.value == -1:
                print("Motor is at minimum range")
                print("To Turn back, press the other button")
                            
except KeyboardInterrupt:
    print("You have stopped motor operation")





