class Solution(object):    def integerReplacement(self, n):        """        :type n: int        :rtype: int        """        def helper(n,step):            if n==1:                return step            if n%2==0:                return helper(int(n/2),step+1)            else:                return min(helper(n+1,step+1),helper(n-1,step+1))        step=0        step=helper(n,step)        return steps=Solution()n=8print(s.integerReplacement(n))