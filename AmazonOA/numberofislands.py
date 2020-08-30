import collections
def numberofislands(grid):
    if not grid or not grid[0]:
        return 0
    m = len(grid)
    n = len(grid[0])
    visited = set()
    count = 0
    directions = [[-1,0],[1,0],[0,1],[0,-1]]
    q= collections.deque()
    for i in range(m):
        for j in range(n):
            visited.add((i,j))
            if grid[i][j]=='1':
                q.append([i,j])
                while q:
                    x,y = q.popleft()
                    for direction in directions:
                        newx,newy = x+direction[0], y + direction[1]
                        if 0<=newx<m and 0<=newy<n and (newx,newy) not in visited:
                            visited.add((newx,newy))
                            if grid[newx][newy]=='1':
                                grid[newx][newy]='*'
                                q.append([newx,newy])
                count +=1
    return count
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(numberofislands(grid))


