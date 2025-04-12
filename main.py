import time 

#Have a start command for timer
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

def pomodoro():
    #Greeting message to intro Pomodoro timer
    start = input("Welcome to your Pomodoro session. Ready to start? (Yes/No)".title())
    while True:
        if start == "No":
            print("No problem! Relaunch again when you're ready to start.")
            break
        elif start != "Yes" and start != "No":
            print("Invalid response. Please try again.")
            continue
        else:
            

pomodoro()