image = input('Initial image:')
message = input('message to encode:')
file = 'encodedMessage.ppm'
writer = open(file,'w')

messes = ""

tmpbyte = bin(len(message))[2:]

sizeheaderbytes = 3

while len(tmpbyte)<8*sizeheaderbytes:
  tmpbyte="0"+tmpbyte
messes+=tmpbyte

for char in message:
  tempbyte = bin(ord(char))[2:]
  while len(tempbyte)<8:
    tempbyte="0"+tempbyte
  messes+=tempbyte

with open(image, 'r') as ppm:
  data = ppm.read()

lines = data.split('\n')

writer.writelines(lines[0]+" "+lines[1])
writer.writelines('\n')
lines = lines[2:]

imgsize = lines[0].split(' ')

writer.writelines(lines[0]+" "+lines[1])
writer.writelines('\n')
lines = lines[2:]

for line in lines:
    vals = ""
    for num in line.split(' '):
        if not num=="":
            if len(messes)>0:
              if(eval(num) <= 1):
                vals+=messes[:1]
              else:
                vals+=str(int(bin(eval(num))[2:len(bin(eval(num)))-1] + messes[:1],2))
              #print bin(eval(num))[2:len(bin(eval(num)))-1] + messes[:1]
              #print bin(eval(num))[2:]
              messes = messes[1:]
            else:
              vals+=num
            vals+=" "
            #raw_input()
    #print vals
    writer.writelines(vals)
    writer.writelines('\n')

print "Done!"
#bits of message stored in last bit of color byte of image
#header byte(modular) of length of message
