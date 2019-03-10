class Solution:
    def fourSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dict={}
        res=set()
        n=len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] not in dict:
                    dict[nums[i]+nums[j]]=[(nums[i],nums[j],i,j)]
                elif (nums[i],nums[j]) not in dict[nums[i]+nums[j]]:
                    dict[nums[i]+nums[j]].append((nums[i],nums[j],i,j))
        #print(dict)
        for i in range(n):
            for j in range(i+1,n):
                t=target-nums[i]-nums[j]
                if t in dict:
                    for k in dict[t]:
                        if j<k[2]:
                            res.add((nums[i],nums[j],nums[k[2]],nums[k[3]]))
        return [list(i) for i in res]
nums = [1,0,-1,0,-2,2]
target = 0

print(Solution.fourSum(nums, target))