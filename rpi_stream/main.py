import RPi.GPIO as GPIO
import time
import os

twt_btn = 11
utb_btn = 7
led = 40
twt_press = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(twt_btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(utb_btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(twt_press, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, False)
while True:
    try:
        print("Twitter {} Youtube {}".format(GPIO.input(twt_btn), GPIO.input(utb_btn)))
        if GPIO.input(twt_btn) and not GPIO.input(utb_btn):
            GPIO.output(led, True)
            time.sleep(0.5)
            GPIO.output(led, False)
            time.sleep(0.5)
            os.system("sudo python ./send_to_twitter.py")
            print("Twitter activated")
            break
        elif not GPIO.input(twt_btn) and GPIO.input(utb_btn):
            #os.system("sudo sh ./live_youtube.sh")
            for i in range(3):
                GPIO.output(led, True)
                time.sleep(0.5)
                GPIO.output(led, False)
                time.sleep(0.5)
            os.system("sudo sh ./live_local.sh")
        
            print("Local / youtube activated")
            break
        else:
            time.sleep(5)
    except:
        pass
    
