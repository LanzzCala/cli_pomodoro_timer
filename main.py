import time 

#Greeting message to intro Pomodoro timer
#Have a start command for timer
#Display timer in MM:SS format
#Need a timer that visually counts down at 25 mins
#Timer stops at 25 mins and starts 5 min rest timer
#Display pomodoro is starting
#Alarm/notification for starting
#Display pomodoro is ending
#Alarm/notification for ending
#Pause timer feature
#Display feature for repeat

def pomodoro():
    print("Welcome to your Pomodoro session. Ready to start?")
    print (time.localtime())

pomodoro()