class Solution(object):    def maxProduct(self, nums):        """        :type nums: List[int]        :rtype: int        """        if len(nums)==0:            return        ans=nums[0]        max1,min1=nums[0],nums[0]        for i in range(1,len(nums)):            max1,min1=max(max1*nums[i],min1*nums[i],nums[i]),min(max1*nums[i],min1*nums[i],nums[i])            ans=max(max1,ans)        return ansnums=[-4,-3,-2]s=Solution()print(s.maxProduct(nums))#乘法的话要记录max和min