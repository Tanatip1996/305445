import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 501
MESSAGE = input("Enter a number: ")

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(str(MESSAGE), (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print 'Server response : ' + data


