#!/usr/bin/env python


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
            arr = x.split(',', 7);
            i = 2;
            while i < 8:
                print (arr[i])
                i += 1
