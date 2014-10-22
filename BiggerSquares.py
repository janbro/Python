#Reduce n to prime factors
#Perform brute force on smallest prime
#Scale grid to n

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

n = 49

primfacs = primes(n)

smallestPrim = primfacs[0]

print primfacs

#Base prime number square(Brute forcer goes here)
squares = [1,1,2,3,1,1,3,2,1,1,3,1,2,3,1,3,3,1] #3
squares = [1,1,1,1,2,1,2,1,1,2,2,1] #2
squares = [1,1,2,1,3,2,3,1,1,4,1,1,3,2,2,5,1,3,4,4,4,1,5,3,3,4,1] #7

#Scaler
scaledSquares = [1,1]
for x in xrange(2,len(squares)):
    scaled = squares[x]
    if (x-2)%3==0:
        scaled = squares[x]*primfacs[0]
        print squares[x]
    else:
        for pr in primfacs[1:]:
            scaled*=pr
        scaled-=(n%2+1)
    scaledSquares.append(scaled)

print scaledSquares
