class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        if n<=1: return n
        if n==2: return 1+(A[0]!=A[1])
        ans,cur=1,2
        for i in range(1,n-1,1):
            if(A[i]-A[i-1])*(A[i]-A[i+1])>0:
                cur+=1
            else:
                ans,cur=max(ans,cur),2
        return max(ans,cur)



s1=Solution()
