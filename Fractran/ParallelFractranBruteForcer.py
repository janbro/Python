import pp
from fractions import Fraction
import math
def parallel_function(arg):
    return arg

job_server = pp.Server()


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

def lps(start,rang,fractran,abso,floats,pows,strf,Fraction):
    for q1 in xrange(start,rang):
        for p1 in xrange(2,rang):
            if abso(q1/p1-floats(q1)/p1)>0:
                for q2 in xrange(1,rang):
                    for p2 in xrange(2,rang):                    
                        if abso(q2/p2-floats(q2)/p2)>0:
                            for q3 in xrange(1,rang):
                                for p3 in xrange(2,rang):
                                    if abso(q3/p3-floats(q3)/p3)>0:
                                        for q4 in xrange(1,rang):
                                            for p4 in xrange(2,rang):
                                                if abso(q4/p4-floats(q4)/p4)>0:
                                                    for q5 in xrange(1,rang):
                                                         for p5 in xrange(2,rang):                    
                                                            if abso(q5/p5-floats(q5)/p5)>0:
                                                                for q6 in xrange(1,rang):
                                                                    for p6 in xrange(2,rang):
                                                                        if abso(q6/p6-floats(q6)/p6)>0:
                                                                            sequence = ""+strf(q1)+" / "+strf(p1)+","+strf(q2)+" / "+strf(p2)+","+strf(q3)+" / "+strf(p3)+","+strf(q4)+" / "+strf(p4)+","+strf(q5)+" / "+strf(p5)+","+strf(q6)+" / "+strf(p6)
                                                                            if fractran(pows(2,3)*pows(3,2),sequence,35) == 6103515625:
                                                                                job_server.submit(parallel_function, (("Sequence: "+sequence),))
                                        

# Define your jobs
job1 = job_server.submit(lps, (1,200,fractran,abs,float,pow,str,Fraction))
job2 = job_server.submit(lps, (5,200,fractran,abs,float,pow,str,Fraction))
job3 = job_server.submit(lps, (7,200,fractran,abs,float,pow,str,Fraction))
job4 = job_server.submit(lps, (9,200,fractran,abs,float,pow,str,Fraction))
job5 = job_server.submit(lps, (11,200,fractran,abs,float,pow,str,Fraction))
job6 = job_server.submit(lps, (13,200,fractran,abs,float,pow,str,Fraction))

# Compute and retrieve answers for the jobs.
print job1()
print job2()
print job3()
print job4()
print job5()
print job6()
