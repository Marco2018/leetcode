import copy
class Solution:
    def maxDistance(self, grid):
        n = len(grid)
        visited = [[0 for i in range(n)] for j in range(n)]
        level = []
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    level.append([i, j])
                    visited[i][j] = 1
        if len(level) == 0 or len(level) == n*n: return -1
        next_level = []
        d = 0
        while level or next_level:
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while level:
                i, j = level.pop(0)
                for ii, jj in dirs:
                    if i+ii>=0 and i+ii<n and j+jj>=0 and j+jj<n and visited[i+ii][j+jj] == 0:
                        next_level.append([i+ii, j+jj])
                        visited[i+ii][j+jj] = 1
            level = copy.deepcopy(next_level)
            next_level = []
            if level:
                d += 1
        return d