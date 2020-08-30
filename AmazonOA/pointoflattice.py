def pointoflattice(ax,ay,bx,by):
    if ay==by:
        return (bx,by-(bx-ax>0))
    if ax==bx:
        return (bx+(by-ay>0),by)
    dx = bx - ax
    dy = by - ay
    rx = dy
    ry = -dx
    maxgcd = abs(gcd(rx,ry))
    rx //= maxgcd
    ry //= maxgcd
    return (bx+rx,by+ry)

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
ax=-1
ay=3
bx=-1
by=5
print(pointoflattice(ax,ay,bx,by))








