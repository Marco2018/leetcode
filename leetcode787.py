class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src==dst: return 0
        status = K + 1
        dp = [[float("inf") for i in range(n)]  for j in range(status+1)]
        dp[0][src] = 0
        for i in range(1,status+1):
            for s, d, value in flights:
                dp[i][d] = min(dp[i][d], dp[i-1][d], dp[i-1][s]+value)

        if dp[status][dst] == float("inf"):
            return -1
        return dp[status][dst]
        
            
        