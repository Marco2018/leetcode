class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m==0:return 0
        n, res = len(grid[0]), 0
        rows, cols =[0 for i in range(m)], [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rows[i]+=1
                    cols[j]+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if rows[i]>=2 or cols[j]>=2:
                        res+=1
        return res
            
        