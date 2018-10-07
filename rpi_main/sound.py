import pygame.mixer
from threading import Thread
from time import sleep

sounds = {
		'Entrance' : "s1.mp3",
		'YES' : "s2.mp3",
		'NO' : "s3.mp3",
}

def playMusic(soundKey):
	Thread(target = play, args = [soundKey,]).start()
	print "playing now:", sounds[soundKey]

def play(soundKey):
	pygame.mixer.init()
	if pygame.mixer.music.get_busy():
        	return
	pygame.mixer.music.load("/home/pi/R2D2V2-backup/sound_files/"+sounds[soundKey])
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
               	continue
