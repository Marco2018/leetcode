class Solution:    def isInterleave(self, s1, s2, s3):        """        :type s1: str        :type s2: str        :type s3: str        :rtype: bool        """        m,n=len(s1),len(s2)        if n+m!=len(s3):            return False        dp=[[False for i in range(m+1)]for j in range(n+1)]        dp[0][0]=True        for i in range(n+1):            for j in range(m+1):                if i>0:                    dp[i][j]=dp[i][j] or (dp[i-1][j] and s2[i-1]==s3[i+j-1])                if j>0:                    dp[i][j]=dp[i][j] or (dp[i][j-1] and s1[j-1]==s3[i+j-1])        return dp[n][m]