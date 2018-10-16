import time
import serial
from threading import Thread

num = 0
available = False

HAPPY = '1'
DANGER = '2'
DANCE = '3'
LOVE = '4'
SPEAK = '5'

while True:
    try:
        if not available:
            print("Trying serial ACM" + str(num))
            ser = serial.Serial(
                port='/dev/ttyACM'+ str(num),
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)
            available = True
        break
    except:
        if num < 10:
            num += 1
        else:
            break

def send_to_arduino(message):
    try:
        if available:
            print("Sending", message)
            Thread(target=ser.write, args=[message,]).start()
    except:
        pass
