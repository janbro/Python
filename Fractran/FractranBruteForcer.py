from fractions import Fraction
import math
 
def fractran(n, fstring, lim):
    flist = [Fraction(f) for f in fstring.replace(' ', '').split(',')]
 
    n = Fraction(n)
    while True:
        if lim == 0:
            return -1
        for f in flist:
            if (n * f).denominator == 1:
                break
        else:
            break
        n *= f
        lim-=1
    return n

rang = 10

for q1 in xrange(1,rang):
    for p1 in xrange(2,rang):
        if abs(q1/p1-float(q1)/p1)>0:
            for q2 in xrange(1,rang):
                for p2 in xrange(2,rang):                    
                    if abs(q2/p2-float(q2)/p2)>0:
                        for q3 in xrange(1,rang):
                            for p3 in xrange(2,rang):
                                if abs(q3/p3-float(q3)/p3)>0:
                                    sequence = ""+str(q1)+" / "+str(p1)+","+str(q2)+" / "+str(p2)+","+str(q3)+" / "+str(p3)
                                    
                                    if fractran(4,sequence,15) == 9:
                                        print "Sequence: "+sequence
                                        p1 = rang
                                        p2 = rang
                                        p3 = rang
                                        q1 = rang
                                        q2 = rang
                                        q3 = rang
                        
 
if __name__ == '__main__':
    n, m = 4, 15
    print('First %i members of fractran(%i):\n  ' % (m, n) +
          ', '.join(str(f) for f,i in zip(fractran(n,sequence), range(m))))
