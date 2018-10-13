from motor import Motor

class Move():
        step = 15
	directionFunction = { 1 : moveForward, -1 : moveBackward, 2 : moveClockwise, -2:moveCounterClockwise, 3 : moveLeft, 4 : moveRight }

	def __init__(self, leftMotor, rightMotor, headMotor):
		self._leftMotor = leftMotor
		self._rightMotor = rightMotor
		self._headMotor = headMotor
                self.direction = 0
                self.current_speed = 0
		self.current_turningspeed = 0

        def increase_speed(self, max_speed):
                self.current_speed += max_speed / Move.step
                if (self.current_speed > max_speed):
                    self.current_speed = max_speed

        def decrease_speed(self, max_speed):
                self.current_speed -= max_speed / Move.step
                if (self.current_speed < 0):
                    self.current_speed = 0

        def forward(self, speed):
                self.direction = 1
                self.increase_speed(speed)
                self.moveForward()

	def backward(self, speed):
                self.direction = -1
                self.increase_speed(speed)
		self.moveBackward()

	def left(self, speed):
		self.direction = 3
		self.increase_speed(speed)
		self.moveLeft()

	def right(self, speed):
		self.direction = 4
		self.increase_speed(speed)
		self.moveRight()

	def turnClockwise(self, speed):
		direction = 2
		self.increase_speed(speed)
		self.moveClockwise()

	def turnCounter(self, speed):
		direction = -2
		self.increase_speed(speed)
		self.moveCounterClockwise()

	def stop(self, max_speed):
		if self.current_speed == 0:
			self._leftMotor.stop()
			self._rightMotor.stop()
		else:
			self.decrease_speed(max_speed)
			self.directionFunction[self.direction]()
		self._headMotor.stop()

	def domeClockwise(self, headSpeed):
		self._headMotor.clockwise(headSpeed)

	def domeCounter(self, headSpeed):
		self._headMotor.counterClockwise(headSpeed)

	def moveForward(self):
		self._leftMotor.clockwise(self.current_speed)
		self._rightMotor.clockwise(self.current_speed)

	def moveBackward(self):
               	self._leftMotor.counterClockwise(self.current_speed)
		self._rightMotor.counterClockwise(self.current_speed)

	def moveClockwise(self):
		self._leftMotor.counterClockwise(self.current_speed)
		self._rightMotor.clockwise(self.current_speed)

	def moveCounterClockwise(self):
		self._leftMotor.clockwise(self.current_speed)
		self._rightMotor.counterClockwise(self.current_speed)

	def moveLeft(self):
                self._leftMotor.clockwise(0.75*self.current_speed)
                self._rightMotor.clockwise(self.current_speed)

	def moveRight(self):
		self._leftMotor.clockwise(self.current_speed)
		self._rightMotor.clockwise(0.75*self.current_speed)


