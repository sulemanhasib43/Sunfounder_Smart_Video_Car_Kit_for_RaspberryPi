#!/usr/bin/env python


# GGA - essential fix data which provide 3D location and accuracy data.

#  $GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47

# $GPGGA,,,,,,0,00,99.99,,,,,,*48





# 0
# 00,99.99,,,,,,*48



#     pi@raspberrypi:~/git/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server $ ./serial_read.py 
# ./

# 3342.23820
# N
# 07258.76586
# E
# 1
# 04,2.22,609.6,M,-40.6,M,,*7D

# $GPGGA,110917.00,3342.23906,N,07258.76593,E,1,04,2.22,611.0,M,-40.6,M,,*72

# 3342.23906
# N
# 07258.76593
# E
# 1
# 04,2.22,611.0,M,-40.6,M,,*72



# Where:
#      GGA          Global Positioning System Fix Data
#      123519       Fix taken at 12:35:19 UTC
#      4807.038,N   Latitude 48 deg 07.038' N
#      01131.000,E  Longitude 11 deg 31.000' E
#      1            Fix quality: 0 = invalid
#                                1 = GPS fix (SPS)
#                                2 = DGPS fix
#                                3 = PPS fix
#                                4 = Real Time Kinematic
#                                5 = Float RTK
#                                6 = estimated (dead reckoning) (2.3 feature)
#                                7 = Manual input mode
#                                8 = Simulation mode
#      08           Number of satellites being tracked
#      0.9          Horizontal dilution of position
#      545.4,M      Altitude, Meters, above mean sea level
#      46.9,M       Height of geoid (mean sea level) above WGS84
#                       ellipsoid
#      (empty field) time in seconds since last DGPS update
#      (empty field) DGPS station ID number
#      *47          the checksum data, always begins with *



import time
import serial

# count = 0

def cord():
	# import re

	ser = serial.Serial(
	    port='/dev/ttyAMA0',
	    baudrate=9600,
	    parity=serial.PARITY_NONE,
	    stopbits=serial.STOPBITS_ONE,
	    bytesize=serial.EIGHTBITS,
	    timeout=1
	    )
	# counter = 0
	# global count
	# count += 1 
	# ser = ''
	# if count < 10:
	# 	ser = "$GPGGA,110917.00,3342.33906,N,07258.76593,E,1,04,2.22,611.0,M,-40.6,M,,*72"
	# else:
	# 	ser = "$GPGGA,110917.00,3342.42906,N,07258.76593,E,1,04,2.22,611.0,M,-40.6,M,,*72"
	while True:
		x = ser.readline()
		if "GPGGA" in x:
			lstSer = ser.readline().split(',')
			return lstSer
		 # return (lat,latD,lng, lngD)
	# 	while 1:
	#         x = ser
	#         # x = ser.readline()
	#         if "GPGGA" in x:
	# #            print x
	# #            print re.match(".*?,.*?,\s*(.*?),.*", x).group(1)
	#             arr = x.split(',',6);
	#             i = 2;
	#             # while i < 6:
	#             #     print (arr[i])
	#             #     i += 1

if __name__ == "__main__":
    # cord()pass