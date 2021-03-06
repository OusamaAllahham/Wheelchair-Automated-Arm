"""
Team 37 Servo Control
"""

#imports
from gpiozero import Servo
from gpiozero import Button
import time



print("Program Initiated")


#gpio pin locations
servoPin1 = 17
servoPin2 = 27
button1_pin = 20
button2_pin = 21


'''creating button objects'''
#button1 = Button(button1_pin)
#button2 = Button(button2_pin)

'''Motor Locations'''
#motor1 = Servo(servoPin1, max_pulse_width = 2.7e-3, min_pulse_width = 5e-4)
#motor2 = Servo(servoPin2, max_pulse_width = 2.7e-3, min_pulse_width = 5e-4)

#setting initial click value to 0
init_click_val = 0
b1_clicks = init_click_val
b2_clicks = init_click_val



def button1_clicks(): #counting clicks
        global b1_clicks
        b1_clicks +=1
        return b1_clicks

def button2_clicks(): #counting clicks
        global b2_clicks
        b2_clicks +=1
        return b2_clicks

def run_motor1(): #would have a parameter corresponding to the first motor (motor_1)
    
    if b1_clicks % 2 == 0:
        if button1.is_pressed == True:
            click1 =  button1_clicks() #counting clicks
            print("Button 1 Clicks:"+str(click1)) #displays current count for specific button

        ## iterates forward if motor is not @ max val
        while button1.is_pressed:
            print("Motor 1 is iterating forward..")
            time.sleep(0.5)
            print("Motor 1 is iterating forward...")
            time.sleep(0.5)
            print("Motor 1 is iterating forward....")
            time.sleep(0.5)
            print("Motor 1 is iterating forward...")
            time.sleep(0.5)
            print("Motor 1 is iterating forward..")
            time.sleep(0.5)
        '''
        if motor1.value < 1:
            motor1.value +=0.1
            time.sleep(0.1)
            print("Button 1 is pressed, going forward")
        elif motor1.value ==1:
            print("Motor 1 has reached max upper limit")
        '''
    elif b1_clicks %2 ==1:
        if button1.is_pressed == True:
            click2 = button1_clicks() #counting clicks
            print("Button 1 Clicks:"+str(click2))
            
        ## iterates backward if motor is not @ min val
        while button1.is_pressed:
            print("Motor 1 is iterating backward..")
            time.sleep(0.5)
            print("Motor 1 is iterating backward...")
            time.sleep(0.5)
            print("Motor 1 is iterating backward....")
            time.sleep(0.5)
            print("Motor 1 is iterating backward...")
            time.sleep(0.5)
            print("Motor 1 is iterating backward..")
            time.sleep(0.5)
            
        '''
        if motor1.value > -1:
            motor1.value -= 0.1
            print("Button 1 is pressed, going backwards")
            time.sleep(0.1)
        elif motor1.value == -1:
            print("Motor 1 has reached max lower limit")
        '''
        
        
def run_motor2():

    if b2_clicks % 2 == 0:
        
        if button2.is_pressed == True:
            click1 = button2_clicks() #counting clicks
            print("Button 2 Clicks:"+str(click1))
            
        ## iterates forward if motor is not @ max val
        while button2.is_pressed:
                
            print("Motor 2 is iterating forward..")
            time.sleep(0.5)
            print("Motor 2 is iterating forward...")
            time.sleep(0.5)
            print("Motor 2 is iterating forward....")
            time.sleep(0.5)
            print("Motor 2 is iterating forward...")
            time.sleep(0.5)
            print("Motor 2 is iterating forward..")
            time.sleep(0.5)
            
        '''
        if motor2.value < 1:
            motor2.value += 0.1
            print("Button 2 is pressed, going forwards")
            time.sleep(0.1)
        elif motor2.value == 1:
            print("Motor 2 has reached max upper limit")
        '''
            
    elif b2_clicks % 2 == 1:
        
        if button2.is_pressed == True:        
            click2 = button2_clicks() #counting clicks
            print("Button 2 Clicks:"+str(click2))
        ## iterates backward if motor is not @ min val   
        while button2.is_pressed:
            print("Motor 2 is iterating backward..")
            time.sleep(0.5)
            print("Motor 2 is iterating backward...")
            time.sleep(0.5)
            print("Motor 2 is iterating backward....")
            time.sleep(0.5)
            print("Motor 2 is iterating backward...")
            time.sleep(0.5)
            print("Motor 2 is iterating backward..")
            time.sleep(0.5)
            

        '''
        if motor2.value > -1:
            motor2.value -= 0.1
            print("Button 2 is pressed, going backwards")
            time.sleep(0.1)
        elif motor2.value == -1:
            print("Motor 2 has reached max lower limit")
        '''
  
def main():

    ## resetting motor
    #init_val = -1
    #motor1.value = init_val
    #motor2.value = init_val

    ## running motors
    while True:
        try:
            button1.is_pressed == True #button pressing simulation(1)
            run_motor1() #would call motor_1 object
            run_motor2() #would call motor_2 object
            
        except KeyboardInterrupt:
            print("You have manually stopped motor operation")


if __name__ == "__main__":
    main()
input()
                
    
