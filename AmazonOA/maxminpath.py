def maxminpath(matrix):
    if not matrix or not matrix[0] or (len(matrix)==1 and len(matrix[0])<=1):
        return 0
    n,m = len(matrix),len(matrix[0])
    
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 and j ==0:
                continue
            elif (i==0 and j==1) or (i==1 and j==0):
                dp[i][j]=matrix[i][j]
            elif i ==0:
                dp[i][j]=min(matrix[i][j],dp[i][j-1])
            elif j==0:
                dp[i][j]=min(matrix[i][j],dp[i-1][j])
            else:
                dp[i][j]=min(matrix[i][j],max(dp[i][j-1],dp[i-1][j]))
    print(dp)
    if n==1:
        return dp[0][-2]
    if m==1:
        return dp[-2][0]
    else:
        return max(dp[-2][m-1],dp[n-1][-2])
matrix = [[1, 2, 3],[4, 5, 1]]
print(maxminpath(matrix))



