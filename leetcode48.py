import copyclass Solution:    def rotate(self, matrix):        """        :type matrix: List[List[int]]        :rtype: void Do not return anything, modify matrix in-place instead.        """        n=len(matrix)        if n==0:            return matrix        matrix2=copy.deepcopy(matrix)        for i in range(n):            for j in range(n):                matrix[i][j]=matrix2[n-1-j][i]        returns=Solution()print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))