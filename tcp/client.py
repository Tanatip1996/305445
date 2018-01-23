#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5002
BUFFER_SIZE = 1024
data = input("Enter a number: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(str(data))
data = s.recv(BUFFER_SIZE)
s.close()
print "Resulf of factorial :", data 

