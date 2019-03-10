class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if len(A)<=1 or len(A[0])==0:
            return 0
        m,n=len(A),len(A[0])
        count=0
        for i in range(n):
            for j in range(1,m):
                if A[j-1][i]>A[j][i]:
                    count+=1
                    break
        return count
s1=Solution()
A=["ift","efd","dnete","tef","fdn"]
print(s1.shortestSuperstring(A))
