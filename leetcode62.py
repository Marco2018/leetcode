class Solution:    def uniquePaths(self, m, n):        if n<=0 or m<=0:            return 0        if n==1 or m==1:            return 1        num = [[0 for i in range(m)] for j in range(n)]        for i in range(m):            num[0][i] = 1        for i in range(n):            num[i][0] = 1        for i in range(1, n, 1):            for j in range(1, m, 1):                num[i][j] = num[i - 1][j] + num[i][j - 1]        return num[n - 1][m - 1]s=Solution()n=2m=3print(s.uniquePaths(m,n))