class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid, i, j, isvisited, n, m):
            directions = [[-1,0], [1,0],[0,-1],[0,1]]
            for ii, jj in directions:
                if i+ii<0 or i+ii>=n or j+jj<0 or j+jj>=m:
                    self.touch_corner = True
                else:
                    if grid[i+ii][j+jj] == 0 and isvisited[i+ii][j+jj] == 0:
                        isvisited[i+ii][j+jj] = 1
                        dfs(grid, i+ii, j+jj, isvisited, n, m)
            return
        
        if not grid or len(grid[0]) == 0:
            return 0
        count = 0
        n, m = len(grid), len(grid[0])
        isvisited = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and isvisited[i][j] == 0:
                    isvisited[i][j] = 1
                    self.touch_corner = False
                    dfs(grid, i, j, isvisited, n, m)
                    if not self.touch_corner:
                        count += 1
        return count