class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m,n=len(A),len(A[0])
        dp=[1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if all(A[k][j]<=A[k][i] for k in range(m)):
                    dp[i]=max(dp[i],dp[j]+1)
        return n-max(dp)
s1=Solution()
print(s1.minDeletionSize(["abbba"]))
