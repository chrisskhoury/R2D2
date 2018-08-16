import pygame
from threading import Thread
from time import sleep

sounds = {
		1 : "s1.mp3",
		2 : "s2.mp3",
		3 : "s3.mp3",
		4 : "s4.mp3",
		5 : "s5.mp3",
		6 : "s6.mp3"
}

def Play(soundNum):
	pygame.mixer.init()
	pygame.mixer.music.load(sounds[soundNum])
	pygame.mixer.music.play()

while True:
	Thread(target = playMusic).start()
	print("playing now")
	sleep(5)
