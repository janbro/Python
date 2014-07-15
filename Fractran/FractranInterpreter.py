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

rang = 15

sq1 = []
sq2 = []
sq3 = []
sq4 = []
sq5 = []
sq6 = []
count = 0
for q1 in xrange(1,rang):
    for p1 in xrange(2,rang):
        if abs(q1/p1-float(q1)/p1)>0:
            if q1/p1 not in sq1:
                sq1.append(float(q1)/p1)
                for q2 in xrange(1,rang):
                    for p2 in xrange(2,rang):                    
                        if abs(q2/p2-float(q2)/p2)>0:
                            if q2/p2 not in sq2:
                                sq2.append(float(q2)/p2)
                                for q3 in xrange(1,rang):
                                    for p3 in xrange(2,rang):
                                        if abs(q3/p3-float(q3)/p3)>0:
                                            if q3/p3 not in sq3:
                                                sq3.append(float(q3)/p3)
                                                for q4 in xrange(1,rang):
                                                    for p4 in xrange(2,rang):
                                                        if abs(q4/p4-float(q4)/p4)>0:
                                                            if q4/p4 not in sq4:
                                                                sq4.append(float(q4)/p4)
                                                                for q5 in xrange(1,rang):
                                                                    for p5 in xrange(2,rang):                    
                                                                        if abs(q5/p5-float(q5)/p5)>0:
                                                                            if q5/p5 not in sq5:
                                                                                sq5.append(float(q5)/p5)
                                                                                for q6 in xrange(1,rang):
                                                                                    for p6 in xrange(2,rang):
                                                                                        if abs(q6/p6-float(q6)/p6)>0:
                                                                                            if q6/p6 not in sq6:
                                                                                                count+=1
                                                                                                sq6.append(float(q6)/p6)
                                                                                                sequence = ""+str(q1)+" / "+str(p1)+","+str(q2)+" / "+str(p2)+","+str(q3)+" / "+str(p3)+","+str(q4)+" / "+str(p4)+","+str(q5)+" / "+str(p5)+","+str(q6)+" / "+str(p6)
                                                                                                if count%10000 == 0:
                                                                                                    print count,":",sequence
                                                                                                #print sequence
                                                                                                if fractran(72,sequence,35) == 6103515625:
                                                                                                    print "Sequence: "+sequence
                                        
                        
print 'Done'
if __name__ == '__main__':
    n, m = 4, 15
    print('First %i members of fractran(%i):\n  ' % (m, n) +
          ', '.join(str(f) for f,i in zip(fractran(n,sequence), range(m))))
