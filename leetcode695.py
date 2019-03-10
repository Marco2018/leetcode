import numpy
class Solution(object):
    def maxAreaOfIsland(self, grid):
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]:
                grid[i][j]=0
                return 1+dfs(i-1,j)+dfs(i,j-1)+dfs(i+1,j)+dfs(i,j+1)
            return 0
        maxarea=0
        for i in range(m):
            for j in range(n):
                area=dfs(i,j)
                if area>maxarea:
                    maxarea=area
        return maxarea


"""
class Solution:
    def sumarea(self,i,j,rows,cols,grid,isvisited):
        temp=0
        if i>0 and grid[i-1][j]==1 and isvisited[i-1][j]==0:
            isvisited[i-1][j]=1
            temp+=(self.sumarea(i-1,j,rows,cols,grid,isvisited)+1)
        if j>0 and grid[i][j-1]==1 and isvisited[i][j-1]==0:
            isvisited[i][j-1]=1
            temp+=(self.sumarea(i,j-1,rows,cols,grid,isvisited)+1)
        if i<rows-1 and grid[i+1][j]==1 and isvisited[i+1][j]==0:
            isvisited[i+1][j]=1
            temp+=(self.sumarea(i+1,j,rows,cols,grid,isvisited)+1)
        if j<cols-1 and grid[i][j+1]==1 and isvisited[i][j+1]==0:
            isvisited[i][j+1]=1
            temp+=(self.sumarea(i,j+1,rows,cols,grid,isvisited)+1)
        return temp

    def maxAreaOfIsland(self, grid):

        rows=len(grid)
        cols=len(grid[0])
        maxarea=0
        for i in range(rows):
            for j in range(cols):
                isvisited = numpy.zeros((rows,cols))
                if grid[i][j]==1:
                    isvisited[i][j]=1
                    temp_area=1
                    temp_area+=self.sumarea(i,j,rows,cols,grid,isvisited)
                    if temp_area>maxarea:
                        maxarea=temp_area
        return maxarea
"""

solution=Solution()
grid=[[1,0,1],[1,1,1],[0,0,1]]
print(solution.maxAreaOfIsland(grid))

#time limited