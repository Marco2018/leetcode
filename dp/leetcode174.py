class Solution:    def calculateMinimumHP(self, dungeon):        """        :type dungeon: List[List[int]]        :rtype: int        """        n,m=len(dungeon),len(dungeon[0])        if n==0 or m==0:            return 0        inithealth=[[0 for i in range(m)]for j in range(n)]        for i in range(n-1,-1,-1):            for j in range(m-1,-1,-1):                if i==n-1 and j==m-1:                    inithealth[i][j]=max(1,1-dungeon[i][j])                elif i==n-1:                    inithealth[i][j]=max(1,inithealth[i][j+1]-dungeon[i][j])                elif j==m-1:                    inithealth[i][j]=max(1,inithealth[i+1][j]-dungeon[i][j])                else:                    inithealth[i][j]=max(1,min(inithealth[i+1][j],inithealth[i][j+1])-dungeon[i][j])        return inithealth[0][0]s=Solution()dungeon=[[100]]print(s.calculateMinimumHP(dungeon))1 为什么要从后往前？因为从前往后算dp 可能会出现<=0 从后往前考虑比较好2 initheadlth[i][j] 表示的是要进点[i][j]之前所需要的health