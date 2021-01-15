"""
Team 37 Servo Control
"""

#imports
from __future__ import division
from gpiozero import Servo
from gpiozero import Button
import time
import Adafruit_PCA9685



print("Program Initiated")


#gpio pin locations
button1_pin = 20
button2_pin = 21

#creating button objects
button1 = Button(button1_pin)
button2 = Button(button2_pin)


#setting initial click value to 0
init_click_val = 0
b1_clicks = init_click_val
b2_clicks = init_click_val

## init test
pwm = Adafruit_PCA9685.PCA9685()
global servo_min
global servo_max
servo_min = 150
servo_max = 1500
pwm.set_pwm_freq(60)

def button1_clicks(): #counting clicks
        global b1_clicks
        b1_clicks +=1
        return b1_clicks

def button2_clicks(): #counting clicks
        global b2_clicks
        b2_clicks +=1
        return b2_clicks

def test():
        x = servo_min
        
        print("test")
        while True:
            pwm.set_pwm(1,0, servo_min)
            time.sleep(1)
            pwm.set_pwm(1,0,servo_max)
            if button1.is_pressed:
                print("Button 1 is pressed")
            elif button2.is_pressed:
                print("Button 2 is pressed")
            time.sleep(0.5)
            x += 1
                            

def main():
        while True:
            pwm.set_pwm(1,0, servo_min)
            time.sleep(1)
            pwm.set_pwm(1,0,servo_max)
            time.sleep(1)


if __name__ == "__main__":
    main()

