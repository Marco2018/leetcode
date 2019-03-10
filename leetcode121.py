class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofits=0
        bemin=10000
        n=len(prices)
        if n<2:
            return 0
        for i in range(n):
            if prices[i]<bemin:
                bemin=prices[i]
            elif prices[i]-bemin>maxprofits:
                maxprofits=prices[i]-bemin
        return maxprofits


object=Solution()
prices=[7,1,5]
print(Solution.maxProfit(object,prices))