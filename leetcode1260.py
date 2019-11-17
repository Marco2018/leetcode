import copy
class Solution:
    def shiftGrid(self, grid, k):
        if not grid or len(grid[0]) == 0:
            return
        n, m = len(grid), len(grid[0])
        res = copy.deepcopy(grid)
        for t in range(k):
            for j in range(1, m):
                for i in range(n):
                    res[i][j] = grid[i][j-1]
            # j=0
            for i in range(1, n):
                res[i][0] = grid[i-1][m-1]
            res[0][0] = grid[n-1][m-1]
            grid = copy.deepcopy(res)
        return res