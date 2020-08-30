import collections
def subarraywithdistinct(s,k):
    return atmost(s,k)-atmost(s,k-1)

def atmost(s,k):
    count = collections.Counter()
    i = 0
    res = 0
    for j in range(len(s)):
        if count[s[j]]==0:
            k-=1
        count[s[j]]+=1
        while k<0:
            count[s[i]]-=1
            if count[s[i]]==0:
                k+=1
            i+=1
        res +=j-i+1
    return res
s = "ababa"
k = 3
print(subarraywithdistinct(s,k))



