import socket
import time
import os
import sys
import random
from threading import Thread
from ED import *
#Tcp Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Port to use to connect
port = 5005
host = str(raw_input("What server would you like to connect to? "))
count = 0
print("Connecting to server...")
time.sleep(1)
while count == 0:
	try:
		s.connect((host , port))
		count += 1
	except:
		pass

print "You've Connected Succesfully!!!"

password = str(raw_input("What is your password? "))
passkey = getKey(password)

def listen():
	global s
	global passkey
	while True:	
		time.sleep(1)
		datae = s.recv(1024)
		if datae != "":
			print "Recived message!"
			time.sleep(.01)
			datad = decryption(datae, passkey)
			print str(host) + "> " + str(datad.rstrip(os.linesep))
def Send():
	global s
	global password
	global passkey
	print "Type a message and then press enter"
	while True:
		datad = raw_input("")
		datae = encryption(datad, passkey)
		s.send(datae)
		print "Message sent..."

if __name__ == "__main__":
	Thread(target=listen).start()
	Thread(target=Send).start()