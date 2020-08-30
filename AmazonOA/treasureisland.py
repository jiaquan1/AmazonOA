import collections
def treasureisland(maps):
    m = len(maps)
    n = len(maps[0])
    q = collections.deque()
    visited = set()
    q.append((0,0))
    visited.add((0,0))
    step = 0
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    while q:
        size = len(q)
        new = []
        print(step,q)
        step+=1
        for i in range(size):
            x,y = q.pop()
            for d in directions:
                newx,newy = x+d[0],y+d[1]
                if 0<=newx<m and 0<=newy<n and (newx,newy) not in visited:
                    visited.add((newx,newy))
                    if maps[newx][newy]=='O':
                        new.append((newx,newy))
                    elif maps[newx][newy]=='X':
                        return step
                    
        q= new
maps = [['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

print(treasureisland(maps))




