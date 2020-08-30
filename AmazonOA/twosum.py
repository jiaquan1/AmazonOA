def twosum(nums,target):
    if not nums or len(nums)==1:
        return Null
    dic = {}
    res = []
    for i,x in enumerate(nums):
        
        if target -30-x in dic:
            res.append([dic[target-30-x],i])
        dic[x]=i
    return res[-1] if res else Null
nums = [0,0,0]
target = 30
print(twosum(nums,target))




