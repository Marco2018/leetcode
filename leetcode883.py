class Solution:    def projectionArea(self, grid):        """        :type grid: List[List[int]]        :rtype: int        """        if not grid:            return 0        count=0        n=len(grid)        row=[0 for i in range(n)]        col=[0 for i in range(n)]        for i in range(n):            index_row=-float("inf")            index_col=-float("inf")            for j in range(n):                if grid[i][j]!=0:                    count+=1                index_row=max(index_row,grid[i][j])                index_col=max(index_col,grid[j][i])            row[i]=index_row            col[i]=index_col        return sum(row)+sum(col)+counts=Solution()grid=[[1,2],[3,4]]print(s.projectionArea(grid))