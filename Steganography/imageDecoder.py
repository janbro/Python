image = input('Image to decode: ')

reader = open(image,'r')

sizeheaderbyte = 3

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
        if count>6*sizeheaderbyte:
            break
        if not num=="":
            messlength+=str(bin(eval(num))[len(bin(eval(num)))-1])
        count+=1

messlength = int(messlength,2)

byte=''

count = 0
#Extract message, read only up to relevant character
for line in lines:
    for num in line.split(' '):
        if count>(messlength+1)*7:
            break
        if not num=="":
            byte+=str(bin(eval(num))[len(bin(eval(num)))-1])
            count+=1

messbytes = list(chunks(byte,7))

secretmessage = ""

for x in xrange(1,int(messbytes[0],2)+1):
    #print byte
    #raw_input()
    #print chr(int(messbytes[x],2)),
    secretmessage+=chr(int(messbytes[x],2))
print secretmessage
