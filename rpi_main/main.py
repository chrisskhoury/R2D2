import RPi.GPIO as GPIO

import time
import cwiid
import os

from sound import Play
from move import Move

GPIO.setmode(GPIO.BOARD)

#speed control
speed = 50
turningSpeed = 37

#global status = "-----"

#initializing the variables
R_EN1 = 7
L_EN1 = 11
RPWM1 = 3
LPWM1 = 5

R_EN2 = 36
L_EN2 = 32
RPWM2 = 40
LPWM2 = 38

'''
pinA = 1
pinB = 2
pinC = 3
'''

# used for the sleep function between each reading from the wii remote
button_delay = 0.1

status = "Pair Wii"

print ('Press 1 + 2 on your Wii Remote now ...')
time.sleep(1)

# Connect to the Wii Remote. If it times out
try:
	wii = cwiid.Wiimote()

except RuntimeError:
	print ("Error opening wiimote connection")
	status = "Error, retry"
	os.system("sudo python main.py")
	quit()

print ('Wii Remote connected...\n')
print ('Press some buttons!\n')
print ('Press PLUS and MINUS together to disconnect and quit.\n')

status = "Success"

wii.rpt_mode = cwiid.RPT_BTN

playMusic('Entrance')

for i in range (1,5):
	wii.rumble = 1
	time.sleep(0.05)
	wii.rumble = 0
	time.sleep(0.05)
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
			left(speed, turningSpeed)
			time.sleep(button_delay)

		if(buttons & cwiid.BTN_RIGHT):
			print ('Right pressed')
			right(speed, turningSpeed)
			time.sleep(button_delay)

		if (buttons & cwiid.BTN_UP):
			print ('Up pressed')
			forward(speed)
			time.sleep(button_delay)

		if (buttons & cwiid.BTN_DOWN):
			print ('Down pressed')
			backward(speed)
			time.sleep(button_delay)

		if (buttons & cwiid.BTN_PLUS):
			print ('Plus Button pressed')
			turnClockwise(speed)
			time.sleep(button_delay)

		if (buttons & cwiid.BTN_MINUS):
			print ('Minus Button pressed')
			turnCounter(speed)
			time.sleep(button_delay)
		
		if (buttons & cwiid.BTN_A):
			print ('Button B pressed')
			playMusic('YES')
			time.sleep(button_delay)

		if (buttons & cwiid.BTN_B):
			print ('Button B pressed')
			playMusic('NO')
			time.sleep(button_delay)
		
		if (not buttons):
			stop()
except:	
	print ("Error opening wiimote connection")
	status = "Error, retry"
	os.system("sudo python main.py")
	quit()
