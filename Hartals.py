#Multiples of political parties numbers
#Not on days divisible by 7 or (/7)-1
#count days, subtract days on fri/sat
day = 100
multiples = [7*x for x in xrange(0,day/7)]
for x in xrange(0,len(multiples)):
    multiples.insert(x,multiples[x]-1)

parties = [12,15,25,40]
tot = 0
for num in parties:
    tot+=day/num
    for mult in multiples:
        if mult%num==0:
            tot-=1

print tot
