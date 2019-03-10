class Solution(object):
    def numIslands(self, grid):
        if grid==[]:
            return 0
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]=='1':
                grid[i][j]='0'
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
            return

        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
        return count
solution=Solution()
grid1=[]
grid=[['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
print(solution.numIslands(grid1))
