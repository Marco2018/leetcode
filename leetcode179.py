from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def cmp(x,y):
            if x+y<y+x:
                return 1
            elif x+y>y+x:
                return -1
            return 0
        if sum(nums)==0:
            return "0"
        nums_str=[str(x) for x in nums]
        nums_str.sort(key=cmp_to_key(cmp))
        return "".join(x for x in nums_str)
s1=Solution()
nums =[3,30,34,5,9]
print(s1.largestNumber(nums))