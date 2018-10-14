from picamera import PiCamera
from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep
import tweepy

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
      formatted_name = '/home/pi/PhotoBooth/' + str(current_time.year) + str(current_time.month) + str(current_time.day)
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
      camera.annotate_text = ""
      camera.capture(pic_path)
      sleep(0.3)
      GPIO.add_event_detect(eff_button, GPIO.RISING, bouncetime = 250)
      api.update_with_media(pic_path, status="Pictures from the Coder-Maker photobooth! #rpi #codermaker")

cap_button = 32
eff_button = 40
effects = {0:'none', 1:'oilpaint', 2:'cartoon', 3:'pastel', 4:'emboss', 5:'gpen', 6:'solarize', 7:'negative', 8:'sketch'}
current_effect = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(eff_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(cap_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(cap_button, GPIO.RISING, bouncetime = 4000, callback = cheese)
GPIO.add_event_detect(eff_button, GPIO.RISING, bouncetime = 250)

try:
      with PiCamera() as camera:
            camera.annotate_text_size = 130
            camera.start_preview()
            camera.hflip = True
            while True:
                  if GPIO.event_detected(eff_button):
                        current_effect = (current_effect + 1) % 9
                        camera.image_effect = effects[current_effect]
                  sleep(0.25)

            camera.stop_preview()
finally:
      GPIO.cleanup()
