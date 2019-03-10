class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        a,b,i=1,2,2
        while n>i:
            a,b=b,a+b
            i=i+1
        return b
object1=Solution()
n=3
print(Solution.climbStairs(object1,n))