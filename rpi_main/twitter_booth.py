from picamera import PiCamera
from datetime import datetime
from time import sleep
import tweepy
import os

consumer_token = 'kXHI7ZM7DRc1FARaBQwFRKmbe'
consumer_secret = 'NTzXeoYY7wJlAAIxHbA8A434kwyCROlQQi5lf2OtldqNsffgz2'

access_token = '954690971798827009-Znn3WSvQL5P30UxKB91FuqeCG2Ebt9f'
access_token_secret = 'EERoJ8yblc4JUdw9rFYQzgbBbxqmM501VPvrC8RdoKUpj'

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

target_folder = "/home/pi/Photobooth/"

api = tweepy.API(auth)

def getName():
      if not os.path.exists(target_folder):
            os.makedirs(target_folder)
      current_time = datetime.now()
      formatted_name = target_folder + str(current_time.year) + str(current_time.month) + str(current_time.day)
      formatted_name += '_' + str(current_time.hour) + str(current_time.minute)
      formatted_name += str(current_time.second) + '.jpg'
      return formatted_name

def takePicture(caption:str):
      pic_path = getName()
      with PiCamera() as camera:
            camera.capture(pic_path)
      api.update_with_media(pic_path, status=caption)  