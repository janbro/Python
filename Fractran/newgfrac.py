from fractions import Fraction
import math

#Prime Factor
def primes(n):
    if n == 1:
        return [1]
    try:
        if "/" in n:
            return 'X '+str(primes(n[0]))+" / "+str(primes(n[2]))
    except:
        num = n
        primfac = []
        d = 2
        while d*d <= n:
            while (n % d) == 0:
                primfac.append(d)  # supposing you want multiple factors repeated
                n /= d
            d += 1
        if n > 1:
           primfac.append(n)
       
        d = [str(key)+"^"+str(primfac.count(key)) for key in set(primfac)]
    
        return d
    
 #1 / 3,35 / 2,5 / 7
def fractran(n, fstring= '9 / 2'): #Program input
    flist = [Fraction(f) for f in fstring.replace(' ', '').split(',')]
 
    n = Fraction(n)
    while True:
        yield n.numerator
        for f in flist:
            if (n * f).denominator == 1:
                break
        else:
            break
        #Fraction NF is integer
        #yield f.numerator,"/",f.denominator,"\n"
        n *= f
 
if __name__ == '__main__':
    n, m = pow(2,5), 15000
    print('First %i members of fractran(%i):\n  ' % (m, n) +
          '  '.join(str(primes(f))+'\n' for f,i in zip(fractran(n), range(m))))
