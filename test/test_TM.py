# coding=utf-8

"""This file shows some use of the rpi_TM1638 librairy"""

from time import sleep
from rpi_TM1638 import TMBoards

# my GPIO settings
# (one TM1638 board connected to GPIO19 for dataIO, GPIO13 for Clock, and GPIO26 for the STB)
STB = 22
CLK = 21
DIO = 17
# STB = 6, 26   # in case you have two TM1638 boards, connected to GPIO06 and GPIO26


myLeds = [False]*8
myLeds[0] = True

# instanciante my TMboards
TM = TMBoards(DIO, CLK, STB, 0)
TM.brightness[0] = 5
#TM.clearDisplay()

# some LEDs manipulation
#TM.leds[12] = True      # turn on led 12 (5th led of the 2nd board, since there is 8 leds per board)

#TM.segments[1] = '0'        # display '0' on the display 1 (2nd 7-segment display of the 1st board)
#TM.segments[4] = '98.76'     # display '9876' on the 7-segment display number 4, 5, 6 and 7 (the point is on segment 5)
#TM.segments[3, 1] = True     # turn on the segment #1 of the 7-segment number 3

#TM.segments[0] = '01234567'
#TM.segments[0] = 'Niclas70'
count = 8597
o = 0
n = 1
b = 0
dir = 1
while True:
#  TM.segments[0] = 'OK  ' if TM.switches[0] else '    '
#  TM.segments[4] = '    ' if TM.switches[1] else 'OK  '
  count += 1
  cstr = '{:08d}'.format(abs(count)%100000000)
  TM.segments[0] = cstr
  tmp = count
  for i in range(8):
    TM.leds[7-i] = tmp & 0b1
    tmp >>= 1
  n = (count >> 3) & 0b1 
  if n != o:
    o = n
    if dir == 1:
      if b == 6:
        dir = 0
      b += 1
    else:
      if b == 1:
        dir = 1
      b -= 1
    TM.brightness[0] = b & 0x7
  sleep(0.05)
