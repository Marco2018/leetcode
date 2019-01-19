class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp=[0]*K
        dp[0]=1
        sum1,count=0,0
        for i in range(len(A)):
            sum1+=A[i]
            count+=dp[sum1%K]
            dp[sum1%K]+=1
        return count

s1=Solution()
print(s1.subarraysDivByK([8,9,7,8,9],8))