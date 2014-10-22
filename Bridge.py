class car:
    def __init__(self, time, weight):
        self.time = time
        self.weight = weight
    def __cmp__(self, other):
        return cmp(self.time, other.time)
    def __repr__(self):
        return repr([self.time, self.weight])

time = [10,30,5,10,20,30,28,3,8,10]#[10,25,5,15,23,20,25,30]
weight = [42,23,40,2,1,4,6,28,17,35]#[10,5,40,35,12,30,42,8]

convoy = [car(time[x],weight[x]) for x in xrange(0,len(weight))][::-1]
convoy = sorted(convoy,None,None,True)
print convoy

totTime=0

for c in convoy:
    tot=c.weight
    con=[c]
    for n in convoy[1:]:
        if tot+n.weight<42:
            tot+=n.weight
            convoy.remove(n)
            con.append(n)
    convoy = convoy[1:]
    totTime+=max(con).time
print totTime
