image = input('Image to decode: ')

reader = open(image,'r')

sizeheaderbyte = 0

with open(image, 'r') as ppm:
  data = ppm.read()

lines = data.split('\n')

lines = lines[2:]


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

#Extract message length
messlength = ''
count = 0
for line in lines:
    for num in line.split(' '):
        if count>8*sizeheaderbyte:
            break
        if not num=="":
            messlength+=str(bin(eval(num))[len(bin(eval(num)))-1])
        count+=1

messlength = int(messlength,2)
messlength = 10000
sizeheaderbyte = 0
byte=''

count = 0
#Extract message, read only up to relevant character
for line in lines:
    for num in line.split(' '):
        if count>(messlength+sizeheaderbyte)*8-1:
            break
        if not num=="":
            byte+=str(bin(eval(num))[len(bin(eval(num)))-1])
            count+=1
            
messbytes = list(chunks(byte,8))[sizeheaderbyte:]
print messbytes

secretmessage = ""

for x in xrange(0,messlength):
    #print byte
    #raw_input()
    #print chr(int(messbytes[x],2)),
    secretmessage+=chr(int(messbytes[x],2))
print secretmessage
