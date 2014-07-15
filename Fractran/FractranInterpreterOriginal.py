from fractions import Fraction
import math

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
    
 #7 / 31,289 / 2,91 / 289,527 / 91,961 / 17,12505 / 33,11 / 61,1 / 11,3 / 41,11 / 7,1 / 3
def fractran(n, fstring= '2/1331,1183/726,121/169,1/363,65/121,33/91,13/11,121/13,161051/2,1/3'):# / 22,11 / 13,1 / 11,2 / 7,55 / 3,1 / 2'):
    flist = [Fraction(f) for f in fstring.replace(' ', '').split(',')]
 
    n = Fraction(n)
    while True:
        yield n.numerator
        for f in flist:
            if (n * f).denominator == 1:
                break
        else:
            break
        yield f.numerator,"/",f.denominator,"\n"
        n *= f
 
if __name__ == '__main__':
    n, m = pow(2,3)*pow(3,3), 150
    print('First %i members of fractran(%i):\n  ' % (m, n) +
          '  '.join(str(primes(f))+'\n' for f,i in zip(fractran(n), range(m))))

