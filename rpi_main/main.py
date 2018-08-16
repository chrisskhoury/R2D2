import RPi.GPIO as GPIO

import time
import cwiid
import os

from sound import Play
from move import Move

GPIO.setmode(GPIO.BOARD)

#speed control
speed=50
turningSpeed=37

global status = "-----"

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

Play('Entrance')

for i in range (1,5):
	wii.rumble = 1         
	time.sleep(0.05) 
	wii.rumble = 0
	time.sleep(0.05)
 
while True:

	buttons = wii.state['buttons']          # get the state of the buttons

	# If Plus and Minus buttons pressed
	# together then rumble and quit.

	if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
		print '\nClosing connection ...'
		wii.rumble = 1
		time.sleep(1)
		wii.rumble = 0
		exit(wii)
    
	if (buttons & cwiid.BTN_LEFT):         # if left button is pressed -> motor1 moves forward
		print 'Left pressed'
		left(speed, turningSpeed)
		time.sleep(button_delay)

	if(buttons & cwiid.BTN_RIGHT):         # if right button is pressed -> motor1 moves backwards
		print 'Right pressed'
		right(speed, turningSpeed)
		time.sleep(button_delay)
    
	if (buttons & cwiid.BTN_UP):           # if up button is pressed -> motor2 moves forward
		print 'Up pressed'
		forward(speed)
		time.sleep(button_delay)   
    
	if (buttons & cwiid.BTN_DOWN):         # if down button is pressed -> motor2 moves backwards
		print 'Down pressed'
		backward(speed)
		time.sleep(button_delay)

	if (buttons & cwiid.BTN_PLUS):         # if (+) button is pressed -> motor3 moves forward
		print 'Plus Button pressed'
		turnClockwise(speed)
		time.sleep(button_delay)
    
	if (buttons & cwiid.BTN_MINUS):        # if (-) button is pressed -> motor3 moves backwards
		print 'Minus Button pressed'
		turnCounter(speed)
		time.sleep(button_delay)

    
  	if (buttons & cwiid.BTN_A):            # if button B is pressed -> motor5 and motor6 moves backward
		print 'Button B pressed'
    		Play('YES')
		time.sleep(button_delay)

    	if (buttons & cwiid.BTN_B):            # if button B is pressed -> motor5 and motor6 moves backwards
		print 'Button B pressed'
		Play('NO')
		time.sleep(button_delay)

	if (not buttons):                      # if there are no buttons pressed -> turn off all motors
		stop() 
