import time 
import os

#Timer stops at 25 mins
#Timer starts 5 min rest timer
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
        elif start != "Yes" and start != "No":
            print(f"You entered {start} which is an invalid response. Please try again.")
            continue
        else:
            os.system("cls")
            seconds = 5
            print ("Let's start. Starting in 5 seconds.")
            time.sleep(2)
            os.system("cls")
            while seconds:
                print (seconds)
                time.sleep(1)
                os.system("cls")
                seconds -=1
            return start

def pomodoro_start(start):
    if start == "No":
        return None
    else:
        #Need a timer that visually counts down at 25 mins
        mins = 0
        seconds = 5
        timer_start = True
        print ("Starting your Pomodoro timer!") #Display pomodoro is starting
        time.sleep(2)
        while timer_start == True:
            time.sleep(1)
            os.system("cls")
            if mins != 0 and seconds == 0:
                mins -= 1
                seconds = 59
                print (f"{mins}:{seconds:02}")#Display timer in MM:SS format
            elif seconds != 0:
                seconds -= 1
                print (f"{mins}:{seconds:02}")#Display timer in MM:SS format
            elif mins == 0 and seconds == 0:
                print ("Done!")
                timer_start = False
                os.system("cls")
        pomodoro_5_min_break(timer_start)


def pomodoro_5_min_break(timer_start):
    if timer_start == False:       
        print("Break time!")
        mins = 5
        seconds = 0
        timer_start = True
        while timer_start == True:
            time.sleep(1)
            os.system("cls")
            if mins != 0 and seconds == 0:
                mins -= 1
                seconds = 59
                print (f"{mins}:{seconds:02}")#Display timer in MM:SS format
            elif seconds != 0:
                seconds -= 1
                print (f"{mins}:{seconds:02}")#Display timer in MM:SS format
            elif mins == 0 and seconds == 0:
                print ("Back to work")
                timer_start == False
                break



pomodoro_start(pomodoro_intro())