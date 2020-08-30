def maxpali(s):
    if not s:
        return ''
    maxlen = 1
    start = 0
    end = 1
    DP =[[False for _ in range(len(s))] for _ in range(len(s))]
    
    for j in range(len(s)):
        for i in range(j+1):
            if (s[i]==s[j]) and (j-i<2 or DP[i+1][j-1]):
                DP[i][j]=True
            if DP[i][j] and j-i+1>maxlen:
                maxlen = j-i+1
                start = i
                end = j+1
                
    return s[start:end]
s="babad"
print(maxpali(s))








