from motor import Motor

class Move():
        step = 15
	def __init__(self, leftMotor, rightMotor, headMotor):
		self._leftMotor = leftMotor
		self._rightMotor = rightMotor
		self._headMotor = headMotor
                self.direction = 0
                self.current_speed = 0

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

	def left(self, speed, turningSpeed):
                self._leftMotor.clockwise(turningSpeed)
                self._rightMotor.clockwise(speed)

	def right(self, speed, turningSpeed):
		self._leftMotor.clockwise(speed)
		self._rightMotor.clockwise(turningSpeed)

	def turnClockwise(self, speed):
		direction = 2
		self.increase_speed(speed)
		self.moveClockwise()

	def turnCounter(self, speed):
		direction = -2
		self.increase_speed(speed)
		self.moveCounterClockwise()

	def stop(self, max_speed):
                self.decrease_speed(max_speed)
                if self.direction == 1:
			self.moveForward()
			self.direction = 1
                elif self.direction == -1:
			self.moveBackward()
			self.direction = -1
                elif self.direction == 2:
			self.moveClockwise()
			self.direction = 2
		elif self.direction == -2:
			self.moveCounterClockwise()
			self.direction = -2
		else:
		    self._leftMotor.stop()
		    self._rightMotor.stop()
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

