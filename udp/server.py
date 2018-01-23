import socket
import math

UDP_IP = "127.0.0.1"
UDP_PORT = 5015
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    factorial = math.factorial(int(data))
    print "Factorial:", factorial
    sock.sendto(str(factorial),addr)
    
    

