class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = [0] * (len(nums) + 1)
        for i in nums:
            seen[i] = 1
        return [i for i in range(1,len(nums)+1) if not seen[i]]