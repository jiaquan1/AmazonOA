def partitionLabels(S):
    rightmost = {c:i for i,c in enumerate(S)}
    left,right = 0,0
    res = []
    for i, x in enumerate(S):
        right = max(right,rightmost[x])
        if i == right:
            res.append(right-left+1)
            left = i+1
    return res
S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))


