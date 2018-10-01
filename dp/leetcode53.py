class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return
        sum1,index=0,nums[0]
        for i in range(len(nums)):
            sum1+=nums[i]
            if sum1>index:
                index=sum1
            if sum1<0:
                sum1=0
        return index
object1=Solution()
nums=[-2,-1]
print(Solution.maxSubArray(object1,nums))