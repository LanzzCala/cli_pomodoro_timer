import time 
import os

#Timer stops at 25 mins
# Timer starts 5 min rest timer
#Display pomodoro is starting
#Alarm/notification for starting
#Display pomodoro is ending
#Alarm/notification for ending
#Pause timer feature
#Display feature for repeat

def pomodoro_intro():
    #Greeting message to intro Pomodoro timer
    while True:
        #Have a start command for timer
        start = input("Welcome to your 25 minute Pomodoro session. Ready to start? (Yes/No) ").capitalize()
        if start == "No":
            print("No problem! Relaunch again when you're ready to start.")
            return start
            break
        elif start != "Yes" and start != "No":
            print(f"You entered {start} which is an invalid response. Please try again.")
            continue
        else:
            print ("Let's start.")
            return start

def pomodoro_start(start):
    if start == "No":
        return None
    else:
        #Need a timer that visually counts down at 25 mins
        mins = 1
        seconds = 3
        #Display timer in MM:SS format
        print (f"Starting at {mins}:{seconds:02}")
        while True:
            #Have delay countdown to start pomodoro timer
            time.sleep(1)
            os.system("cls")
            if mins != 0 and seconds == 0:
                mins -= 1
                seconds = 59
                print (f"{mins}:{seconds:02}")
            elif seconds != 0:
                seconds -= 1
                print (f"{mins}:{seconds:02}")
            elif mins == 0 and seconds == 0:
                print ("Done!")
                break



pomodoro_start(pomodoro_intro())