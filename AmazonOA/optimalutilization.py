import collections
import itertools
def optimalutilization(a,b,target):
    adict= collections.defaultdict(list)
    bdict= collections.defaultdict(list)
    for e in a:
        adict[e[1]].append(e[0])
    for e in b:
        bdict[e[1]].append(e[0])
    avalue = sorted(list(adict.keys()))
    bvalue = sorted(list(bdict.keys()))
    pa,pb = 0,len(bvalue)-1
    sumdict = collections.defaultdict(list)
    maxsum =-float('inf')
    while pa<len(avalue) and pb>=0:
        s = avalue[pa]+bvalue[pb]
        if s<=target:
            if s>=maxsum:
                maxsum =s 
                sumdict[s].append([avalue[pa],bvalue[pb]])
            pa +=1
        else:
            pb -=1
    res = []
    for pair in sumdict[maxsum]:
        aindex = adict[pair[0]]
        bindex = bdict[pair[1]]
        res+= list(itertools.product(aindex,bindex))
    return res if res else [[]]
a = [ [1, 5], [2, 5], [3,7]]
b=[ [1, 5], [2, 5] ,[3,3]]
target= 10

print(optimalutilization(a,b,target))


