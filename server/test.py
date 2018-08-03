#!/usr/bin/env python

from gps import cord
from socket import *

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-',
            'xy_home']

# top = Tk()  # Create a top window
# top.title('Sunfounder Raspberry Pi Smart Video Car')

HOST = '10.10.0.111'  # Server(Raspberry Pi) IP address
PORT = 8000
BUFSIZ = 1024  # buffer size
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)  # Create a socket
tcpCliSock.connect(ADDR)  # Connect with the server


# =============================================================================
# The function is to send the command forward to the server, so as to make the 
# car move forward.
# ============================================================================= 
def forward_fun(event):
    print 'forward'
    tcpCliSock.send('forward')

arr = cord()
lat = arr[2]
latD= arr[3]
lng = arr[4]
lngD= arr[5]
print (lat,latD,lng, lngD)

dlat = float(lat) + 0.10 # destination lat
dlatD =latD # same as current lat direction
dlng = lng # same as current lng
dlngD = lngD # same as current lng direction

while True:
	current = cord()
	currLat = float(current[2])
	currLatD = current[3]
	currLng = current[4]
	currLngD = current[5]

	if currLat <= dlat:
		forward_fun(0)
		print (currLat)
	else:
		break

