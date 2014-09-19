from fractions import Fraction
import math
 
def fractran(n, fstring='35 / 4,6 / 5,9 / 2,5 / 21'):
    flist = [Fraction(f) for f in fstring.replace(' ', '').split(',')]
 
    n = Fraction(n)
    while True:
        yield n.numerator
        for f in flist:
            if (n * f).denominator == 1:
                break
        else:
            break
        n *= f
 
if __name__ == '__main__':
    n, m = math.pow(2,2)*math.pow(3,3), 150
    print('First %i members of fractran(%i):\n  ' % (m, n) +
          ', '.join(str(f) for f,i in zip(fractran(n), range(m))))
