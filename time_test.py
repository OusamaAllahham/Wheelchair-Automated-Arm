"""
testing time
"""
#imports
import time


def button1_count():
    global x
    x = 5
    start_time = time.time()
    while x > 0:
        x -=1
        time.sleep(0.5)
        pass
    elapsed_time = round(abs(start_time - time.time()),2)

    
    return elapsed_time


def main():
    
    count = button1_count()
    print("Time recorded: "+str(count)+" seconds")

if __name__ == "__main__":
    main()
