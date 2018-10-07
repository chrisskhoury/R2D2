import RPi.GPIO as GPIO

import time
import cwiid
import os

from threading import Thread
from motor import Motor,L293d,Driver
from sound import playMusic
from move import Move

from send_to_arduino import *

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#speed control
speed = 50
turningSpeed = 37
headSpeed = 100

#global status = "-----"

#initializing the variables

RPWM1 = 3
LPWM1 = 5

RPWM2 = 40
LPWM2 = 38

LPWM3 = 10
RPWM3 = 8

led = 37
GPIO.setup(led,GPIO.OUT)

# used for the sleep function between each reading from the wii remote
button_delay = 0.1

leftMotor = Driver(RPWM1, LPWM1)
rightMotor = Driver(RPWM2, LPWM2)
headMotor = Driver(RPWM3, LPWM3)

move = Move(leftMotor, rightMotor, headMotor)

#status = "Pair Wii"

print ('Press 1 + 2 on your Wii Remote now ...')
time.sleep(1)
GPIO.output(led,True)

# Connect to the Wii Remote. If it times out
try:
        GPIO.output(led,True)
	wii = cwiid.Wiimote()

except RuntimeError:
	print ("Error opening wiimote connection .. Try again")
	#status = "Error, retry"
	time.sleep(1)
	os.system("sudo python /home/pi/R2D2V2-backup/rpi_main/main.py")
	quit()
	
GPIO.output(led,False)
print ('Wii Remote connected...\n')
print ('Press some buttons!\n')
print ('Press PLUS and MINUS together to disconnect and quit.\n')

#status = "Success"

wii.rpt_mode = cwiid.RPT_BTN

playMusic('Entrance')

for i in range (1,7):
	wii.rumble = 1
	time.sleep(0.5)
	wii.rumble = 0
	time.sleep(0.05)
curret_btn = 0
try:
        while True:

                buttons = wii.state['buttons']

                # If Plus and Minus buttons pressed
                # together then rumble and quit.

                if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
                        print ('\nClosing connection ...')
                        wii.rumble = 1
                        time.sleep(1)
                        wii.rumble = 0
                        exit(wii)

                if (buttons & cwiid.BTN_LEFT):
                        print ('Left pressed')
                        move.left(speed, turningSpeed)
                        time.sleep(button_delay)

                if(buttons & cwiid.BTN_RIGHT):
                        print ('Right pressed')
                        move.right(speed, turningSpeed)
                        time.sleep(button_delay)

                if (buttons & cwiid.BTN_UP):
                        print ('Up pressed')
                        move.forward(speed)
                        Thread(target=send_to_arduino, args=HAPPY).start()
                        time.sleep(button_delay)
                        

                if (buttons & cwiid.BTN_DOWN):
                        print ('Down pressed')
                        move.backward(speed)
                        Thread(target=send_to_arduino, args=DANCE).start()
                        time.sleep(button_delay)

                if (buttons & cwiid.BTN_PLUS):
                        print ('Plus Button pressed')
                        move.turnClockwise(speed)
                        Thread(target=send_to_arduino, args=DANGER).start()
                        time.sleep(button_delay)

                if (buttons & cwiid.BTN_MINUS):
                        print ('Minus Button pressed')
                        move.turnCounter(speed)
                        Thread(target=send_to_arduino, args=LOVE).start()
                        time.sleep(button_delay)
                
                if (buttons & cwiid.BTN_A):
                        print ('Button A pressed')
                        #playMusic('YES')
                        move.domeClockwise(headSpeed)
                        time.sleep(button_delay)

                if (buttons & cwiid.BTN_B):
                        print ('Button B pressed')
                        #playMusic('NO')
                        move.domeCounter(headSpeed)
                        time.sleep(button_delay)
                
                if (not buttons):
                        move.stop()
                        
except:	
	print ("Error with main .. Try again")
	#status = "Error, retry"
	move.stop()
	GPIO.output(led,0)
	time.sleep(1)
	os.system("sudo python /home/pi/R2D2V2-backup/rpi_main/main.py")
