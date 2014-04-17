import math
integer = input("Input a non-negative integer:")
for n in range(3, integer+1):
    found = False
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            found = True
            print n, 'equals', x, '*', n/x
            break # Break in python is like the one in C.
    if found == False:
        # The else on a loop is executed after the loop exits normally, but
        # not when it exits prematurely with a break.
        print n, 'is a prime number'
