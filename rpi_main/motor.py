from abc import ABC, abstractmethod
import RPi.GPIO as GPIO

class Motor(ABC):
	def __init__(self):
		pass

	@abstractmethod
	def clockwise(self, speed, checkMotor):
		pass
	
	@abstractmethod
	def counterClockwise(self, speed, checkMotor):
		pass
	
	@abstractmethod
	def stop():
		pass

class L293d(Motor):
	def __init__(self, pinE, pinA, pinB):
		self._pinE = pinE
		self._pinA = pinA
		self._pinB = pinB
		
		GPIO.setup(pinE, GPIO.OUT)
		GPIO.setup(pinA, GPIO.OUT)
		GPIO.setup(pinB, GPIO.OUT)

		self._pwmE = GPIO.PWM(pinE, 100)
		self._pwmE.start(0)

	def clockwise(self, speed):
		GPIO.output(self._pinE , True)
		GPIO.output(self._pinA , True)
		GPIO.output(self._pinB , False)
		self._pwmE.ChangeDutyCycle(speed)

	def counterClockwise(self, speed):
		GPIO.output(self._pinE , True)
		GPIO.output(self._pinA , False)
		GPIO.output(self._pinB , True)
		self._pwmE.ChangeDutyCycle(speed)

	def stop(self):
		GPIO.output(self._pinE , False)
		GPIO.output(self._pinA , False)
		GPIO.output(self._pinB , False)
		self._pwmE.ChangeDutyCycle(0)

class Driver(Motor):
	def __init__(self):
		self._R_EN = R_EN
		self._L_EN = L_EN
		self._RPWM = RPWM
		self._LPWM = LPWM

		GPIO.setup(R_EN, GPIO.OUT)
		GPIO.setup(L_EN, GPIO.OUT)
		GPIO.setup(RPWM, GPIO.OUT)
		GPIO.setup(LPWM, GPIO.OUT)

		self._pwmR = GPIO.PWM(RPWM, 100)
		self._pwmL = GPIO.PWM(LPWM, 100)
		self._pwmR.start(0)
		self._pwmL.start(0)

	def clockwise(self, speed):
		GPIO.output(self._R_EN, True)
		GPIO.output(self._L_EN, True)
		self._pwmR.ChangeDutyCycle(speed)
		self._pwmL.ChangeDutyCycle(0)

	def counterClockwise(self, speed):
		GPIO.output(self._R_EN, True)
		GPIO.output(self._L_EN, True)	
		self._pwmR.ChangeDutyCycle(0)
		self._pwmL.ChangeDutyCycle(speed)

	def stop():
		GPIO.output(self._R_EN, False)
		GPIO.output(self._L_EN, False)
		self._pwmR.ChangeDutyCycle(0)
		self._pwmL.ChangeDutyCycle(0)
