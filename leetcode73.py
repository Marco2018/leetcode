class Solution:    def setZeroes(self, matrix):        """        :type matrix: List[List[int]]        :rtype: void Do not return anything, modify matrix in-place instead.        """        if len(matrix)==0 or len(matrix[0])==0:            return        n,m=len(matrix),len(matrix[0])        cols,rows=[],[]        for i in range(n):            for j in range(m):                if matrix[i][j]==0:                    cols.append(i)                    rows.append(j)        for item in cols:            for j in range(m):                matrix[item][j]=0        for item in rows:            for i in range(n):                matrix[i][item]=0        return