import picamera
import time
import socket

#for easier typing, replaces the full name by 'camera'
def liveStream():
    camera = picamera.PiCamera() 
    #setting up camera options
    camera.resolution = (720, 480)
    camera.framerate=24

    try:
    	#preparing for network connection
    	server_socket = socket.socket()

    #the stream is at the pi's IP address port 8000
	server_socket.bind(('0.0.0.0', 8000))
    except:
	print("Port is already in use... quitting.")
	exit()

    #listens on the port and waits for someone to attempt connecting    
    try:
        server_socket.listen(0)

    	#the code accepts only one connection and makes a temp file
    	connection=server_socket.accept()[0].makefile('wb')
	#once a connection is established start streaming for 10mins
   	#the stream can be stopped earlier by interrupting
    	#which VLC will do when closing its connection
        camera.start_recording(connection, format='h264')
        camera.wait_recording(6000)
    
    #if an exception occurs or once streaming is done
    #close connection
    finally:
		camera.stop_recording()
	        camera.close()	
		connection.close()
        	server_socket.close()
		print("Camera stop error")
liveStream()
