

import math
def permutationsequence(n,k):
    nums = [i for i in range(1,n+1)]
    ans = ''
    k -= 1
    for i in range(1,n+1):
        n -= 1
        index,k = divmod(k, math.factorial(n))
        ans += str(nums[index])
        nums.remove(nums[index])
    return ans








n= 3
k=3

print(permutationsequence(n,k))





