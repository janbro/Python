#First 3 bytes of header = file extension
#Second set of bytes = message length(length of message length bytes is determined by size of carrier file
#Over encoding - Once the end of the carrier file is reached, start encoding at the beggining of the second to last bit on each byte in the carrier file
import os
import sys
import base64
from math import log

carrierImage = input("Input carrier image:")

insertFile = input("Input file to be encoded:")

outputFile= open('encodedImage.ppm','w')

ext = os.path.splitext(insertFile)[-1].lower()[1:]

header = ""

for ascii in ext: #Encode extension
    temp = ""
    temp += bin(ord(ascii))[2:]
    while len(temp)<8:
        temp="0"+temp
    header+=temp

imageSize = os.path.getsize(carrierImage)
insertSize = os.path.getsize(insertFile)
if imageSize/8<insertSize:
    print "Carrier Image is too small!!"
    sys.exit()

def bytes_needed(n):
     if n == 0:
         return 1
     return int(log(n, 256)) + 1
    
lenByteSize = bytes_needed(imageSize) #Encode message length

temp = bin(insertSize)[2:]

while len(temp)<lenByteSize*8:
    temp="0"+temp
    
header+=temp

print header

with open(insertFile, 'rb') as f:
    insertContents = f.read()
    
insertContentsBinary = header

for char in insertContents:
  tempbyte = bin(ord(char))[2:]
  while len(tempbyte)<8:
    tempbyte="0"+tempbyte
  insertContentsBinary+=tempbyte

print "Contents converted"

with open(carrierImage, 'r') as ppm:
  data = ppm.read()

for line in data.split('\n')[:4]:
    outputFile.writelines(line)
    outputFile.writelines('\n')

lines = data.split('\n')[4:]

for line in lines:
    vals = ""
    for num in line.split(' '):
        if not num=="":
            if len(insertContentsBinary)>0:
              if(eval(num) <= 1):
                vals+=insertContentsBinary[:1]
              else:
                vals+=str(int(bin(eval(num))[2:len(bin(eval(num)))-1] + insertContentsBinary[:1],2))
              insertContentsBinary = insertContentsBinary[1:]
            else:
              vals+=num
            vals+=" "
    outputFile.writelines(vals)
    outputFile.writelines('\n')
    
outputFile.close()

print "Done!"
