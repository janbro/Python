integer = input("Input a non-negative integer:")

for n in range(3, integer+1):
    for x in range(2, n+1):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break # Break in python is like the one in C.
        else:
            # The else on a loop is executed after the loop exits normally, but
            # not when it exits prematurely with a break.
            print n, 'is a prime number'
            break
