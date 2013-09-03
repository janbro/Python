file = input('Input filename:')


def readfile():
    line = ''
    for x in open(file, 'r').readlines():
        line += x
        return line

print readfile()