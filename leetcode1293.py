import heapq
class Solution:
    def shortestPath(self, grid, k):
        n, m = len(grid), len(grid[0])
        dp = [[[float("inf") for a in range(m+1)] for i in range(n+1)] for j in range(k+1)]
        q = [(0, 1, 1)]
        dp[0][1][1] = 0
        stopped = {(1, 1): 0}
        while q:
            dist, i, j = heapq.heappop(q)
            for ii, jj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0 < i+ii<= n and 0 < j+jj <= m and grid[i+ii-1][j+jj-1] != 1:
                    if (i+ii, j+jj) not in stopped or dist + 1 < stopped[(i+ii, j+jj)]:
                        stopped[(i+ii, j+jj)] = dist + 1
                        dp[0][i+ii][j+jj] = dist + 1
                        heapq.heappush(q, (dist + 1, i+ii, j+jj))
        for a in range(1, k+1):
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if grid[i-1][j-1] == 0:
                        dp[a][i][j] = min(min(dp[a][i - 1][j], dp[a][i][j-1]) + 1, dp[a-1][i][j])
                    else:
                        dp[a][i][j] = min(min(dp[a-1][i - 1][j], dp[a-1][i][j-1]) + 1, dp[a-1][i][j])
        if dp[k][n][m] == float("inf"): return -1
        return dp[k][n][m]