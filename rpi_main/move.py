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
                if (self.current_speed < 10):
                    self.current_speed = 0
	
        def forward(self, speed):
                self.direction = 1
                self.increase_speed(speed)
                self._leftMotor.clockwise(self.current_speed)
		self._rightMotor.clockwise(self.current_speed)

	def backward(self, speed):
                self.direction = -1
                self.increase_speed(speed)
		self._leftMotor.counterClockwise(speed)
		self._rightMotor.counterClockwise(speed)
	
	def left(self, speed, turningSpeed):
                self._leftMotor.clockwise(turningSpeed)
                self._rightMotor.clockwise(speed)

	def right(self, speed, turningSpeed):
		self._leftMotor.clockwise(speed)
		self._rightMotor.clockwise(turningSpeed)

	def turnClockwise(self, speed):
		self._leftMotor.counterClockwise(speed)
		self._rightMotor.clockwise(speed)

	def turnCounter(self, speed):
		self._leftMotor.clockwise(speed)
		self._rightMotor.counterClockwise(speed)

	def stop(self, max_speed):
                self.decrease_speed(max_speed)
                if self.direction == 1:
                    self._leftMotor.clockwise(self.current_speed)
                    self._rightMotor.clockwise(self.current_speed)
                elif self.direction == -1:
                    self._leftMotor.counterClockwise(self.current_speed)
                    self._rightMotor.counterClockwise(self.current_speed)
                else:
		    self._leftMotor.stop()
		    self._rightMotor.stop()
		self._headMotor.stop()
	
	def domeClockwise(self, headSpeed):
		self._headMotor.clockwise(headSpeed)

	def domeCounter(self, headSpeed):
		self._headMotor.counterClockwise(headSpeed)
