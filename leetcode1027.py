class Solution:
    def longestArithSeqLength(self, A):
        dp = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                # 站在j处向A[:j+1]探索
                dp[j, A[j]-A[i]] = dp.get((i, A[j]-A[i]), 1) + 1
        return max(dp.values())