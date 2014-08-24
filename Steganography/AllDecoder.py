import os
import sys
import base64
from math import log

inputImage = input("Image to decode:")

reader = open(inputImage,'r')

with open(inputImage, 'r') as ppm:
  data = ppm.read()
  
lines = data.split('\n')[4:]

imageSize = os.path.getsize(inputImage)

def bytes_needed(n):
     if n == 0:
         return 1
     return int(log(n, 256)) + 1
    
lenByteSize = bytes_needed(imageSize)

#Extract header
header = ''
count = (3+lenByteSize)*8

for line in lines:
     for num in line.split(' '):
          if count<=0:
               break
          if not num=="":
               header+=str(bin(eval(num))[len(bin(eval(num)))-1])
               count-=1

def chunks(l, n):
     """ Yield successive n-sized chunks from l.
     """
     for i in xrange(0, len(l), n):
          yield l[i:i+n]

ext = list(chunks(header,8))[:3]
length = int(header[24:],2)

extension = ""

for byte in ext:
    extension+=chr(int(byte,2))

count = 0
byte = ""
#Extract message, read only up to relevant character
for line in lines:
    for num in line.split(' '):
        if count>(length)*8+(3+lenByteSize)*8:
            break
        if not num=="":
            if count >= (3+lenByteSize)*8:
                 byte+=str(bin(eval(num))[len(bin(eval(num)))-1])
            count+=1

messbytes = list(chunks(byte,8))

secretmessage = ""

for byte in messbytes:
    secretmessage+=chr(int(byte,2))

print secretmessage

with open('encodedMessage.'+extension, 'wb') as f:
    f.write(secretmessage)

print 'Done!'
