class Solution:
    def dfs(self, grid, i, j, n, m):
        temp = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for ii, jj in dirs:
            if i+ii>=0 and i+ii<n and j+jj>=0 and j+jj<m:
                if grid[i+ii][j+jj] != 0 and self.visited[i+ii][j+jj] == 0:
                    self.visited[i + ii][j + jj] = 1
                    temp = max(temp, self.dfs(grid, i+ii, j+jj, n, m))
                    self.visited[i + ii][j + jj] = 0
        return temp+grid[i][j]
    def getMaximumGold(self, grid):
        if len(grid) == 0:return 0
        n, m = len(grid), len(grid[0])
        self.visited = [[0 for i in range(m)] for j in range(n)]
        self.res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    self.visited[i][j] = 1
                    temp = self.dfs(grid, i, j, n, m)
                    self.res = max(temp, self.res)
                    self.visited[i][j] = 0
        return self.res