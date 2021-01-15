"""
Team 37 Servo Control
"""

#imports
from gpiozero import Servo
from gpiozero import Button
import time

print("test")


#gpio pin locations
servoPin1 = 17
servoPin2 = 18
button1_pin = 4
button2_pin = 21

#creating button objects
button1 = Button(button1_pin)
button2 = Button(button2_pin)

#motor locations
motor1 = Servo(servoPin1, max_pulse_width = 2.7e-3, min_pulse_width = 5e-4)
motor2 = Servo(servoPin2, max_pulse_width = 2.7e-3, min_pulse_width = 5e-4)

#resetting motor
init_val = -1
motor1.value = init_val
motor2.value = init_val


def run_motor(motor1pin, motor2pin, user_input):
       
        if user_input == "F":
                while button1.is_pressed:
                        if motor1pin.value < 1:
                                motor1pin.value += 0.1
                        time.sleep(0.05)
                        print("Button 1 is pressed ")
                        if motor1pin.value == 1:
                                print("Motor 1 has exceeded maximum range")
                                print("To turn back, press the same button again")
                        if button1.is_pressed == False:
                                break
                        
        if user_input == "F":
                while button2.is_pressed:
                        if motor2pin.value < 1:
                                motor2pin.value += 0.1
                        time.sleep(0.05)
                        print("Button 1 is pressed")
                        if motor2pin.value == 1:
                                print("Motor 2 has exceeded maximum range")
                                print("To turn back, press the same button again")
                        if button2.is_pressed == False:
                                break
 
        if user_input == "B": 
                while button1.is_pressed:
                        if motor1pin.value > -1:
                                motor1pin.value -= 0.1
                        time.sleep(0.05)
                        print("Button 1 is pressed")
                        if motorpin1.value == -1:
                                print("Motor 1 has exceeded minimum range")
                                print("To turn back, press same button again")
                        if button1.is_pressed == False:
                                break
                     
        if user_input == "B":
                while button2.is_pressed:
                        if motor2pin.value > -1:
                                motor2pin.value -= 0.1
                        time.sleep(0.05)
                        print("Button 2 is pressed")
                        if motor2pin.value == -1:
                                print("Motor 2 has exceeded minimum range")
                                print("To turn back, press the same button again")
                        if button2.is_pressed == False:
                                break

def main():
##        global a
##        global b
##        a = 0
##        b = 0
        user_input = input("Enter 'F' for forward and 'B' for backward: ")
        while True: #continuously runs the motor control function

                run_motor(motor1, motor2, user_input)
                time.sleep(0.1)

                

                        
                
                        
