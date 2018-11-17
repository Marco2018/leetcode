class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target-nums[i] in nums:
                ind=nums.index(target-nums[i])
                if i!=ind:
                    return [i,ind]
class Solution:
    def twoSum(self, nums, target):
        dict1={}
        for i in range(len(nums)):
            if target-nums[i] in dict1:
                return [dict1[target-nums[i]],i]
            dict1[nums[i]]=i