#Countdown timer
#Importing timer
import time

#Taking the required time
mytime = int(input("Please input your time in seconds: "))

#Running the timer
while mytime > -1:
    print(mytime)
    time.sleep(1) 
    mytime -= 1
    
#Show it has ended
print("Timer Up!!")
