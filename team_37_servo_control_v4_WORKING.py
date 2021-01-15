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
button1_pin = 16
button2_pin = 21

#creating button objects
button1 = Button(button1_pin)
button2 = Button(button2_pin)

#motor locations
#dont need to be created - just called from microcontroller

#setting initial click value to 0
init_click_val = 0
b1_clicks = init_click_val
b2_clicks = init_click_val

## init setup
pwm = Adafruit_PCA9685.PCA9685()
global servo_min
global servo_max
servo_min = 150
servo_max = 600
pwm.set_pwm_freq(60)

## timing button press
def button1_count():
        start_time = time.time()
        while Button1.is_pressed == True:
                pass
        button_time1 = start_time - time.time()
        return button1_time

## timing button press
def button2_count():
        start_time = time.time()
        while Button2.is_pressed == True:
                pass
        button_time2 = start_time - time.time()
        return button2_time

## calculating position based on time pressed
def button1_position():
        servo_min = 150
        servo_max = 600
        total_range = 450
        time = 5 #need to change - how long in seconds it takes to iterate through range
        time_rotating = button1_count() #how long the motor has rotated for
        pos_per_time = total_range / time
        position = abs(servo_max - (time_rotating * pos_per_time))
        return position


## calculating position based on time pressed
def button2_position():
        servo_min = 150
        servo_max = 600
        total_range = 450
        time = 5 #need to change - how long in seconds it takes to iterate through range
        time_rotating = button2_count() #how long the motor has rotated for
        pos_per_time = total_range / time
        position = abs(servo_max - (time_rotating * pos_per_time))
        return position


## counting clicks
def button1_clicks(): 
        global b1_clicks
        b1_clicks +=1
        return b1_clicks

## counting clicks
def button2_clicks(): 
        global b2_clicks
        b2_clicks +=1
        return b2_clicks

def run_motor1(): ##this is the rewritten function for AdaFruit (hardware ==> sparkfun Servo shield)
    
    if b1_clicks % 2 == 0:
        if button1.is_pressed == True:
            click1 =  button1_clicks() #counting clicks
            print("Button 1 Clicks:"+str(click1))
        
        a = servo_max
        ## iterates forward if motor is not @ max val
        while button1.is_pressed:
                try:
                        pwm.set_pwm(9,0,a)
                        time.sleep(0.1)
                        print("Button 1 is pressed, going forward")
                except:
                        print("Motor 1 has reached max upper limit")
                        
                a +=10
        

    elif b1_clicks %2 ==1:
        if button1.is_pressed == True:
            click2 = button1_clicks() #counting clicks
            print("Button 1 Clicks:"+str(click2))
        a1 = servo_max
        ## iterates backward if motor is not @ min val
        while button1.is_pressed:
                try:
                        pwm.set_pwm(9,0,a1)
                        print("Button 1 is pressed, going backwards")
                        time.sleep(0.1)
                except:
                        print("Motor 1 has reached max lower limit")
                a1 -=10
        
        
def run_motor2():
        
        if b2_clicks % 2 == 0:
                if button2.is_pressed == True:
                    click1 = button2_clicks() #counting clicks
                    print("Button 2 Clicks:"+str(click1))
                b = servo_min            
                ## iterates forward if motor is not @ max val    
                while button2.is_pressed:
                        try:
                                pwm.set_pwm(0,0,b)
                                print("Button 2 is pressed, going forwards")
                                time.sleep(0.1)
                        except:
                                print("Motor 2 has recahed max upper limit")
                         
                        b +=10
                
        elif b2_clicks % 2 == 1:
                if button2.is_pressed == True:
                        click2 = button2_clicks() #counting clicks
                        print("Button 2 Clicks:"+str(click2))
                b1 = servo_max
        ## iterates backward if motor is not @ min val   
                while button2.is_pressed:
                        try:
                                pwm.set_pwm(0,0,b)
                                print("Button 2 is pressed, going backwards")
                                time.sleep(0.1)
                        except:
                                print("Motor 2 has reached max lower limit")
                        b1 -=10




                

def main():
      
        pwm.set_pwm(0,0,servo_min)
       


        ## running motors
        while True:
                try:
                    run_motor1()
                    run_motor2()
                    
                except KeyboardInterrupt:
                    print("You have manually stopped motor operation")


if __name__ == "__main__":
    main()
    

                
    
