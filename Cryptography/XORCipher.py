import os

def checkquotations(stringname):
    if stringname[0] == '"':
        return stringname.strip('""')
    if stringname[0] == "'":
        return stringname.strip("''")
    else:
        return stringname

def encrypt(data, key):
    encryp = ''
    for x in range(0, len(data)):
        encryp += chr(ord(data[x]) ^ ord(key[x]))
    return encryp

def writefile():
    open("encoded.txt", "w").writelines(str(encrypt(data, key)))
    open("key.txt", "w").writelines(str(key))

def readfile(input):
    line = ''
    for x in open((input), 'r').readlines():
        line += x
        return line

while True:
    try:
        file = raw_input("Input filename:")
        file=checkquotations(file)
        if '.txt' in file:
            open(file)
            break
        file+= '.txt'
        open(file)
        break
    except IOError:
        print "File does not exist!"
    except IndexError:
        print "You must specify the message file."

ans = 0
key = 0
data = readfile(file)

while ans != 1:
    ask = raw_input('Do you have your key saved as a .txt file?(yes/no)')
    if ask == "no":
        while True:
            key = raw_input('Input key:')
            try:
                key=checkquotations(key)
                if len(key)<len(data):
                    print "Key length has to be greater than",len(data)
                else:
                    ans=1
                    break
            except IndexError:
                print "You need to input a key."
            except TypeError:
                print "You need to input a key."
    elif ask == "yes":
        while True:
            try:
                key_input = raw_input('Input filename:')
                key_input=checkquotations(key_input)
                if '.txt' in key_input:
                    open(file)
                    key=readfile(key_input)
                    open(key_input).close()
                    ans=1
                    break
                key_input+= '.txt'
                open(file)
                key = readfile(key_input)
                open(key_input).close()
                ans = 1
                break
            except IOError:
                print "File does not exist!"
            except IndexError:
                print "You must specify the key file."
    else:
        print "Please enter yes or no."

os.remove(file)
try:
    writefile()
except TypeError:
    print "Message or key file does not have any readable text!"
open("encoded.txt").close()
