class Solution(object):    def coinChange(self, coins, amount):        """        :type coins: List[int]        :type amount: int        :rtype: int        """        MAX=amount+1        dp=[MAX for i in range(amount+1)]        dp[0]=0        coins.sort()        for item in coins:            for i in range(amount+1):                if i-item>=0:                    dp[i]=min(dp[i-item]+1,dp[i])        if dp[amount]==MAX:            return -1        else:            return dp[amount]coins=[1,2,5]amount=11s=Solution()print(s.coinChange(coins,amount))