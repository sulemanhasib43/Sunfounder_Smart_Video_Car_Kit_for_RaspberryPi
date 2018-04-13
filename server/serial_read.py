#!/usr/bin/env python


# GGA - essential fix data which provide 3D location and accuracy data.

#  $GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47

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

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
counter = 0

while 1:
        x = ser.readline()
        if "GPGGA" in x:
            #print x
            arr = x.split(',', 2);
            i = 2;
            while i < 8:
                print (arr[i])
                i += 1



# #!/usr/bin/python

# str = "1,2,3,4,5,6,7,8,9,8,11,12,13";
# arr = str.split(',', 7);
# i = 2;
# while i < 8:
#     print(arr[i])
#     i += 1


