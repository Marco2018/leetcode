class Solution:
    def maxWidthRamp(self, A):
        s=[]
        res,n=0,len(A)
        for i in range(n):
            if not s or A[s[-1]]>A[i]:
                s.append(i)
        for j in range(n-1,-1,-1):
            while s and A[s[-1]]<=A[j]:
                res=max(res,j-s[-1])
                s.pop()
        return res
s1=Solution()
print(s1.maxWidthRamp([8,8,0,4,1,1,0,1,0,0]))

"""
        n=len(A)
        if n==0:
            return 0
        if A[n-1]>=A[0]:
            return n-1
        else:
            return max(self.maxWidthRamp(A[1:]),self.maxWidthRamp(A[:n-1]))
        TLE
"""
