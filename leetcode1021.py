class Solution:
    def maxScoreSightseeingPair(self, A):
        n = len(A)
        if n <= 1: return 0
        left, index = A[0], 0
        res = 0
        for i in range(1, n):
            if A[i] + left - i + index > res:
                res = A[i] + left - i + index
            if i + A[i] > left + index:
                left, index = A[i], i
        return res
s1=Solution()
res=s1.smallestRepunitDivByK(95)
print(res)