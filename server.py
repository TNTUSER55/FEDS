import socket
import time
import threading
from threading import Thread
import os
from ED import *

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 5005

s.bind(("", port))
s.listen(5)

print "Waiting for connection..."

time.sleep(1)
client, addr = s.accept()

print "Client "+str(addr[0]) + " has connected!!!!"

password = str(raw_input("What is your password? "))
passkey = getKey(password)
start = True
def listen():
	global s
	global client
	global password
	global passkey
	while True:
		datae = client.recv(1024)
		if datae != "":
			print "Recived message!"
			time.sleep(.01)
			datad = decryption(datae, passkey)
			print str(addr[0]) + "> " + str(datad.rstrip(os.linesep))
			
def Send():
	global s
	global client
	global passkey
	while True:
		datad = raw_input("")
		datae = encryption(datad, passkey)
		client.send(datae)




if __name__ == "__main__":
	if start == True:
		print "break if __name__"
		Thread(target=listen).start()
		Thread(target=Send).start()