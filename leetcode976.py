class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(key=lambda x:-x)
        for i in range(len(A)-2):
            if A[i]<A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0

s1=Solution()
print(s1.subarraysDivByK([8,9,7,8,9],8))