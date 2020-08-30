def findlongeststring(data):
    strlen=len(data)
    if strlen ==0:
        return 0
    start,end,vowels=0,strlen-1,set('aeiou')
    for c in data:
        if c in vowels:
             start +=1
        else:
            break
    if start>=strlen:
        return strlen
    while end>=0:
        if data[end] in vowels:
            end -=1
        else:
            break
    bounlen = start+strlen-1-end
    midlen, largest = 0,0
    for c in data[start+1:end+1]:
        if c in vowels:
            midlen+=1
        else:
            midlen=0
        largest=max(largest,midlen)
    return bounlen+largest
A = 'earthproblem'
print(findlongeststring(A))
B = 'letsgosomewhere'
print(findlongeststring(B))







