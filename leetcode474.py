class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if len(strs) == 0:
            return 0
        dp = [[0]*(n+1) for y in range(m+1)]
        for s in strs:
            x = s.count('0')
            y = len(s) - x
            for j in range(m, x-1, -1):
                for k in range(n, y-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-x][k-y]+1)
        return dp[m][n]