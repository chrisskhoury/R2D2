import pygame
from threading import Thread
from time import sleep

sounds = {
		'Entrance' : "s1.mp3",
		'YES' : "s2.mp3",
		'NO' : "s3.mp3",
}

pygame.mixer.init()

def playMusic(soundKey):
	Thread(target = play, args = [soundKey,]).start()
	print("playing now:", soundKey)

def play(soundKey):
	if pygame.mixer.music.get_busy():
        	return
	pygame.mixer.music.load(sounds[soundKey])
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
        	continue
