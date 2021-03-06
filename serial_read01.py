import numpy as np
import serial
import time
import sys
from pylab import *

# open serial port
strPort1 = sys.argv[1];
file1=sys.argv[2];
ser1 = serial.Serial(strPort1, 9600) # Arduino Serial Speed
f=open(file1,"w+")

y=[0]*100
while 1:
  try:
    line = ser1.readline() #read logger data
    data = [float(val) for val in line.split()]
    print(data[0])
    f.write(str(data[0]))
    f.write("\n")
    x=range(0, 100, 1)
    y.insert(0, data[0])
    y.pop(100)
    clf()
    ylim(0, 1200)
    plot(x, y)
    pause(0.05)

  except KeyboardInterrupt:
    print ('exiting')
    break

f.close()
ser1.flush()
ser1.close()