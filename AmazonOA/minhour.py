
 
def minhour(rows,cols,grid):
    if not rows or not cols:
        return 0
    q=[[i,j] for i in range(rows) for j in range(cols) if grid[i][j]==1]
    directions= [[-1,0],[1,0],[0,1],[0,-1]]
    time = 0
    if not q:
        return -1
    while True:
        new = []
        for [i,j] in q:
            for d in directions:
                newi, newj=i+d[0],j+d[1]
                if 0<=newi<rows and 0<=newj<cols and grid[newi][newj]==0:
                    new.append([newi,newj])
                    grid[newi][newj]=1
        q = new
        if not q:
            break
        time +=1
    return time
rows = 4
cols = 5
grid = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]
print(minhour(rows,cols,grid))