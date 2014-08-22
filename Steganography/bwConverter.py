image = input('Initial image:')
file = 'bw.ppm'
writer = open(file,'w')

messes = ""




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
            if(eval(num) <= 127):
              vals+="0"
            else:
              vals+="255"
            vals+=" "
            #raw_input()
    #print vals
    writer.writelines(vals)
    writer.writelines('\n')

print "Done!"
#bits of message stored in last bit of color byte of image
#header byte(modular) of length of message
