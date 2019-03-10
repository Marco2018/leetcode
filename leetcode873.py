class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set(A)
        n = len(A)
        if n <= 2:
            return 0
        res = 2
        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b, length = A[i], A[j], 2
                while a + b in s:
                    a, b, length = b, a + b, length + 1
                res = max(res, length)
        if res > 2:
            return res
        return 0
