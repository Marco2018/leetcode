class Solution:
    def mincostTickets(self, days, costs):
        n = days[-1]
        dp = [0 for i in range(n+31)]
        days = set(days)
        for i in range(30, n+31):
            if i-30 in days:
                dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[-1]