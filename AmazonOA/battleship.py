def battleship(n,s,t):
    battle_ground={}
    ships = s.split(',')
    ships = [s.split(' ') for s in ships]
    shipid=0
    for ship in ships:
        cells = []
        x1,y1 = ship[0][0],ship[0][1]
        x1 = int(x1)-1
        y1 = ord(y1)-65
        x2,y2 = ship[1][0],ship[1][1]
        x2 = int(x2)-1
        y2 = ord(y2)-65
        for x in range(x2-x1+1):
            for y in range(y2-y1+1):
                cells.append((x+x1,y+y1))
        
        battle_ground[shipid]=cells
        shipid+=1
    target = t.split(' ')
    target_cells = []
    for t in target:
        x = t[0]
        y = t[1]
        x = int(x)-1
        y = ord(y)-65
        target_cells .append((x,y))
    
    sunk = 0
    hitnotsunk = 0
    print(target_cells)
    for shipid in battle_ground:
        print (battle_ground[shipid], len(set(battle_ground[shipid])-set(target_cells)), len(set(battle_ground[shipid])))
        if len(set(battle_ground[shipid])-set(target_cells))==0:
            sunk += 1
        elif 0<len(set(battle_ground[shipid])-set(target_cells))<len(set(battle_ground[shipid])):
            hitnotsunk += 1
    return sunk, hitnotsunk
print(battleship(4, "1B 2C,2D 4D","2B 2D 3D 4D 4A"))





