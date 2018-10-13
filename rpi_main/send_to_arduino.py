import time
import serial

num = 0

ser = serial.Serial(
   port='/dev/ttyACM'+ str(num),
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1)

HAPPY = '1'
DANGER = '2'
DANCE = '3'
LOVE = '4'
SPEAK = '5'

def send_to_arduino(message):
   ser.write(message)
   print('Sending ' + message)

