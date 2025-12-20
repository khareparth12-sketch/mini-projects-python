from playsound import playsound
import time

# ANSI characters
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        minutes_left = (seconds - time_elapsed)//60
        seconds_left = (seconds - time_elapsed)%60

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")

    playsound("Project 12/laughing.mp3")

minutes = int(input("How many minutes t wait? "))
seconds = int(input("How many minutes t wait? "))
total_time = minutes*60 + seconds  
alarm(total_time)