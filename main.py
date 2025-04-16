import time 
import os
import keyboard


#Display pomodoro is ending
#Pause timer feature
#Display feature for repeat

pomodoros = 0

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
            print ("Let's start. Starting in 5 seconds.") #Alarm/notification for starting
            time.sleep(2)
            os.system("cls")
            while seconds:
                print (seconds)
                time.sleep(1)
                os.system("cls")
                seconds -=1
            return start

def pomodoro_start(start):
    global pomodoros
    if pomodoros == 4:
        pomodoros = 0
        pomodoro_long_break()
    elif pomodoros != 0:
        pomodoros += 1
    else:
        pomodoro = 0
        pomodoros = pomodoro + 1
    if start == "No":
        return None
    else:
        #Need a timer that visually counts down at 25 mins
        mins = 0
        seconds = 5
        timer_start = True
        print ("Starting your Pomodoro timer!") #Display pomodoro is starting
        time.sleep(1) #Final value at 2
        while timer_start == True:
            time.sleep(1)
            os.system("cls")
            event = keyboard.read_event() # CONTINUE FROM HERE
            if event.event_type == keyboard.KEY_DOWN:
                pause = input("Press space to continue.")
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
        pomodoro_5_min_break(timer_start) #Timer stops at 25 mins 


#Timer starts 5 min rest timer
def pomodoro_5_min_break(timer_start):
    if timer_start == False:
        if pomodoros == 4:
            pomodoro_start(start='Yes')
        else:
            None
        print("Break time!")
        print (f"Pomodoros: {pomodoros}")
        mins = 0
        seconds = 5
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
                time.sleep(1)
                os.system("cls")
                pomodoro_start(start='Yes')

def pomodoro_long_break():
    print("Time for your long break. Great job!")
    mins = 0
    seconds = 10
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
            time.sleep(1)
            os.system("cls")
            pomodoro_start(start='Yes')


pomodoro_start(pomodoro_intro())