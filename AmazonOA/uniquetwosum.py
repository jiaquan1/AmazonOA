def uniquetwosum(nums,target):
    if not nums or len(nums)==1:
        return 0
    ans,comp = set(),set()
    for num in nums:
        c = target - num
        if c in comp:
            res = (c,num) if c<=num else (num,c)
            if res not in ans:
                ans.add(res)
        comp.add(num)
    return len(ans)

nums = [1, 1, 2, 45, 46, 46]
target = 47

print(uniquetwosum(nums,target))
    



