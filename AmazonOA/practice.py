class Solution:
    def countsubsets(self,nums,k):
        res = []
        self.subsets(nums,0,[],res)
        return res
    def subsets(self,nums,index,temp,res):
        if len(nums)>=index and len(temp)>=2:
            res.append(temp[:])
        used = {}
        for i in range(index,len(nums)):
            if i!=0 and nums[i]==nums[i-1]:continue
            print(temp,nums[i])
            if len(temp)>1 and temp[-1]>=nums[i]:
                continue
            # if nums[i] in used:
            #     continue
            used[nums[i]]=True
            temp.append(nums[i])
            self.subsets(nums,i+1,temp,res)
            temp.pop()
a = Solution()
nums = [6,7,7,8]
k = 2
print(a.countsubsets(nums,k))


