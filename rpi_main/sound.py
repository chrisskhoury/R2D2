from threading import Thread
from time import sleep
import os

sounds = {
		'Entrance' : "s3.mp3",
		'YES' : "s2.mp3",
		'NO' : "s1.mp3",
}

def playMusic(soundKey):
	Thread(target = play, args = [soundKey,]).start()
	print "playing now:", sounds[soundKey]

def play(soundKey):
	os.system("omxplayer -o both /home/pi/r2d2v2/sound_files/"+sounds[soundKey])
