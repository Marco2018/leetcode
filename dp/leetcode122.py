class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits=0
        n=len(prices)
        if n<2:
            return 0
        before=prices[0]
        for i in range(1,n):
            if prices[i]>before:
                profits+=prices[i]-before
            before=prices[i]
        return profits


object=Solution()
prices=[7,1,5]
print(Solution.maxProfit(object,prices))