from picamera import PiCamera
from datetime import datetime
from time import sleep
from threading import Thread
import socket
import RPi.GPIO as GPIO
import tweepy

camera = PiCamera()
camera.resolution = (720, 480)
camera.framerate = 24

server_socket = socket.socket()

consumer_token = 'kXHI7ZM7DRc1FARaBQwFRKmbe'
consumer_secret = 'NTzXeoYY7wJlAAIxHbA8A434kwyCROlQQi5lf2OtldqNsffgz2'

access_token = '954690971798827009-Znn3WSvQL5P30UxKB91FuqeCG2Ebt9f'
access_token_secret = 'EERoJ8yblc4JUdw9rFYQzgbBbxqmM501VPvrC8RdoKUpj'

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#used to name picture according to current time
def getname():
	current_time = datetime.now()
	formatted_name = '/home/pi/PhotoBooth/' + str(current_time.year) 
 	formatted_name += str(current_time.month) + str(current_time.day)
	formatted_name += '_' + str(current_time.hour) + str(current_time.minute)
	formatted_name += str(current_time.second) + '.jpg'
	return formatted_name

#counts down, takes picture, and then posts to twitter
def cheese(channel):
	pic_path = getname()
	GPIO.remove_event_detect(eff_button)
	sleep(0.5)
	for i in range(3):
		camera.annotate_text = "\n" + str(3-i)
		GPIO.output(leds[i], True)
		sleep(0.3)
		GPIO.output(leds[i], False)
		sleep(0.7)

	camera.annotate_text = ""
	GPIO.output(leds, True)
	camera.capture(pic_path)
	sleep(0.3)
	GPIO.output(leds, False)
	GPIO.add_event_detect(eff_button, GPIO.RISING, bouncetime = 250)

	api.update_with_media(pic_path, status='Live testing! #rpiphotobooth')  

def liveStream():
	try:
		server_socket.bind(('0.0.0.0', 8000))
	except:
		print("Port already in use... quitting.")
		exit()

	#listens on the port and waits for someone to attempt connecting	
	server_socket.listen(0)
	
	#the code accepts only one connection and makes a temp file
	connection=server_socket.accept()[0].makefile('wb')
	
	#once a connection is established start streaming for 10mins
	#the stream can be stopped earlier by interrupting
	#which VLC will do when closing its connection
	try:
	    camera.start_recording(connection, format='h264')
	    camera.wait_recording(6000)
	#if an exception occurs or once streaming is done
	#close connection
	finally:
	    camera.stop_recording()

cap_button = 12
eff_button = 11
leds = [3,5,7]
effects = {0:'none', 1:'oilpaint', 2:'cartoon', 3:'pastel', 4:'emboss', 5:'gpen', 6:'solarize', 7:'negative', 8:'sketch'}
current_effect = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(eff_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(cap_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(cap_button, GPIO.RISING, bouncetime = 3500, callback = cheese)
GPIO.add_event_detect(eff_button, GPIO.RISING, bouncetime = 250)
GPIO.output(leds, False)

try:

	camera.annotate_text_size = 130
	camera.start_preview()
	while True:
		if GPIO.event_detected(eff_button):
			current_effect = (current_effect + 1) % 9
			camera.image_effect = effects[current_effect]
	 	sleep(0.25)

	camera.stop_preview()
finally:
	GPIO.cleanup()
