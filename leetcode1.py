class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target-nums[i] in nums:
                ind=nums.index(target-nums[i])
                if i!=ind:
                    return [i,ind]
