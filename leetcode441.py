class Solution(object):    def arrangeCoins(self, n):        """        :type n: int        :rtype: int        """        i=1        while i*(i+1)/2<=n:            i+=1        return i-1s=Solution()n=1print(s.arrangeCoins(n))