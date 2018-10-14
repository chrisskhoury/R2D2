import RPi.GPIO as GPIO
import time
import os

twt_btn = 7
utb_btn = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(twt_btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(utb_btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


while True:
    try:
        if GPIO.input(twt_btn) and not GPIO.input(utb_btn):
            #os.system("sudo puthon ./send_to_twitter.py")
            print("Twitter activated")
            time.sleep(5)
            break
        elif not GPIO.input(twt_btn) and GPIO.input(utb_btn):
            os.system("sudo sh ./live_youtube.sh")
            #os.system("sudo sh ./live_local.sh")
            print("Local / youtube activated")
            time.sleep(5)
            break
        else:
            time.sleep(5)
    except:
        pass
    
