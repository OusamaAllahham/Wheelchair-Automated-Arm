"""
Team 37 Servo Control Simulation
DP4
Client: Ryan
"""
#imports

'''
from gpiozero import Servo
from gpiozero import Button
'''
import time



print("Program Initiated")


#gpio pin locations
'''
servoPin1 = 17
servoPin2 = 27
button1_pin = 20
button2_pin = 21
'''


#creating button objects
'''
button1 = Button(button1_pin)
button2 = Button(button2_pin)
'''

#motor locations
'''
motor1 = Servo(servoPin1, max_pulse_width = 2.7e-3, min_pulse_width = 5e-4)
motor2 = Servo(servoPin2, max_pulse_width = 2.7e-3, min_pulse_width = 5e-4)
'''

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

def run_motor1():
        ## motor sim
        f = "Forward"
        b = "Backward"
        button1_clicks()
        print("Running Motor 1....")
        time.sleep(0.5)
        print("Running Motor 1...")
        time.sleep(0.5)
        print("Running Motor 1..")
        time.sleep(0.5)
        print("Running Motor 1.")
        time.sleep(0.5)
        print("Running Motor 1..")
        time.sleep(0.5)
        print("Running Motor 1...")
        time.sleep(0.5)
        print("Running Motor 1....")
        time.sleep(0.5)
        
        while True:
            
                x = button1_clicks()
                print("Button clicks: ", x)
                if x % 2 ==0:
                        print("Motor is running "+f)
                elif x % 2 ==1:
                        print("Motor is running "+b)
                time.sleep(2)
  

                
                
        
def run_motor2():
        
        ## motor sim
        f = "Forward"
        b = "Backward"
        button1_clicks()
        print("Running Motor 2....")
        time.sleep(0.5)
        print("Running Motor 2...")
        time.sleep(0.5)
        print("Running Motor 2..")
        time.sleep(0.5)
        print("Running Motor 2.")
        time.sleep(0.5)
        print("Running Motor 2..")
        time.sleep(0.5)
        print("Running Motor 2...")
        time.sleep(0.5)
        print("Running Motor 2....")
        time.sleep(0.5)
        
        while True:
       
                y = button2_clicks()
                print("Button clicks: ", y)
                if y % 2 ==0:
                        print("Motor is running "+f)
                elif y % 2 ==1:
                        print("Motor is running "+b)
                time.sleep(2)
     
  
def main():

    ## resetting motor
    init_val = -1
    '''
    motor1.value = init_val
    motor2.value = init_val
    '''

    ## running motors
    motor_choice = input("Enter '1' to run Motor 1 and enter '2' to run Motor 2: ")

    if motor_choice == "1":
            while True:
                    try:
                            run_motor1()
                    except:
                            print("Motor 1 has failed")
    elif motor_choice == "2":
            while True:
                    try:
                            run_motor2()
                    except:
                            print("Motor 2 has failed")
   
            
        


if __name__ == "__main__":
    main()
input()
                
    
