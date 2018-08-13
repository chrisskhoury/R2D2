import time
import serial

success = 0
while (not success):
	try:
		i = 0
		ser = serial.Serial(
		   port='/dev/ttyACM' + i,
		   baudrate = 9600,
		   parity=serial.PARITY_NONE,
		   stopbits=serial.STOPBITS_ONE,
		   bytesize=serial.EIGHTBITS,
		   timeout=1)
		i += 1
		success = 1
	except:
		success = 0
		print("Error connecting to Arduino")

def send_to_arduino(message):
   ser.write('Write counter: %s \n'%(message))
   print('Sending ' + message + ' to Arduino')

try:
	send_to_arduino('1')
	time.sleep(2)
	send_to_arduino('2')
	time.sleep(2)
except:
	print("Error sending to Arduino")
