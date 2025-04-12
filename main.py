import time 
import os
#Display timer in MM:SS format
#Have delay countdown to start pomodoro timer
#Need a timer that visually counts down at 25 mins
#Timer stops at 25 mins and starts 5 min rest timer
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
            break
        elif start != "Yes" and start != "No":
            print("Invalid response. Please try again.")
            print (start)
            continue
        else:
            print ("Let's start.")

def pomodoro_start():
    mins = 25
    seconds = 60
    print (f"Starting at {mins}:{seconds}")
    while True:
        time.sleep(1)
        os.system("cls")
        if seconds != 0:
            seconds -= 1
            print (f"{mins}:{seconds}")
        if seconds == 0:
            print ("Done!")
            break



pomodoro_start()