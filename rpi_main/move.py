from Motor import motor

class move():
	def __init__(self, leftMotor, rightMotor, headMotor):
		self._leftMotor = leftMotor
		self._rightMotor = rightMotor
		self._headMotor = headMotor

	def forward(self, speed):
		self._leftMotor.clockwise(speed)
		self._rightMotor.clockwise(speed)

	def backward(self, speed):
		self._leftMotor.counterClockwise(speed)
		self._rightMotor.counterClockwise(speed)
	
	def left(self, speed, turningSpeed):
		self._leftMotor.clockwise(turningSpeed)
		self._rightMotor.clockwise(speed)

	def right(self, speed, turningSpeed):
		self._leftMotor.clockwise(speed)
		self._rightMotor.clockwise(turningSpeed)

	def clockwise(self, speed):
		self._leftMotor.counterClockwise(speed)
		self._rightMotor.clockwise(speed)

	def counter(self, speed):
		self._leftMotor.clockwise(speed)
		self._rightMotor.counterClockwise(speed)

	def stop(self):
		self._leftMotor.stop()
		self._rightMotor.stop()
	
	def domeClockwise(self, headSpeed):
		self._headMotor.clockwise(headSpeed)

	def domeCounter(self, headSpeed):
		self._headMotor.clockwise(headSpeed)
