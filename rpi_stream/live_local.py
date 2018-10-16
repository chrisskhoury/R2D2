## to connect on vlc: tcp/h264://192.168.xxx.xxx:8000

import picamera
import time
import socket
import RPi.GPIO as GPIO
from threading import Thread

cap_led = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(cap_led, GPIO.OUT)

GPIO.output(cap_led, False)
led_pwm = GPIO.PWM(cap_led, 100)
led_pwm.start(0)

stop_blink = False
stop_fade = False

def blink():
    global stop_blink
    while not stop_blink:
        led_pwm.ChangeDutyCycle(0)
        time.sleep(0.2)
        led_pwm.ChangeDutyCycle(100)
        time.sleep(0.2)
        led_pwm.ChangeDutyCycle(0)
        time.sleep(0.2)
        led_pwm.ChangeDutyCycle(100)
        time.sleep(0.2)
        led_pwm.ChangeDutyCycle(0)
        time.sleep(5)
    led_pwm.ChangeDutyCycle(0)
        

def fade_led(delay):
    global stop_fade
    while not stop_fade:
        for i in range(100):
            led_pwm.ChangeDutyCycle(i)
            time.sleep(delay)
        for i in range(100,0,-1):
            led_pwm.ChangeDutyCycle(i)
            time.sleep(delay)
    led_pwm.ChangeDutyCycle(0)
        
#for easier typing, replaces the full name by 'camera'
def liveStream():
    global stop_fade
    global stop_blink
    camera = picamera.PiCamera() 
    #setting up camera options
    camera.resolution = (720, 480)
    camera.framerate=24

    try:
    	#preparing for network connection
    	server_socket = socket.socket()

    #the stream is at the pi's IP address port 8000
	server_socket.bind(('0.0.0.0', 8000))
    except:
	print("Port is already in use... quitting.")
	exit()

    #listens on the port and waits for someone to attempt connecting    
    try:
        server_socket.listen(0)
        blinking = Thread(target=blink)
        blinking.start()
    	#the code accepts only one connection and makes a temp file
    	connection=server_socket.accept()[0].makefile('wb')
	#once a connection is established start streaming for 10mins
   	#the stream can be stopped earlier by interrupting
    	#which VLC will do when closing its connection
        stop_blink = True
        fading = Thread(target=fade_led, args=[0.07,])
        fading.start()
        camera.start_recording(connection, format='h264')
        camera.wait_recording(6000)
    
    #if an exception occurs or once streaming is done
    #close connection
    finally:
                stop_fade = True
		camera.stop_recording()
	        camera.close()	
		connection.close()
        	server_socket.close()
		print("Camera stop error")
liveStream()
