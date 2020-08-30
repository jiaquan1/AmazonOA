def ntozeros(n):
    L,rem = n//2,n%2
    if rem:
        ans=[0]
    else:
        ans=[]
    for i in range(1,L+1):
        ans.append(-i)
        ans.append(i)
    return ans
n = 7
print(ntozeros(n))







