#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
	print "Usage: vrfy.py <file>"
	sys.exit(0)

filename = sys.argv[1]
with open(filename) as file_object:
	for line in file_object:
		# Create a Socket
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Connect to the Server
		connect=s.connect(('10.11.1.115',25))
		# Receive the banner
		banner=s.recv(1024)
		print banner
		# VRFY a user
		s.send('VRFY ' + line )
		result=s.recv(1024)
		print result
		# Close the socket
		s.close()
