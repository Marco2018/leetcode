class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def maxsum(A):
            n,sum1,temp=len(A),-float("inf"),0
            for i in range(n):
                temp+=A[i]
                sum1=max(sum1,temp)
                if temp<0:
                    temp=0
            return sum1
        n=len(A)
        is_allpo,is_allne=1,1
        for i in range(n):
            if A[i]>0:
                is_allne=0
            if A[i]<0:
                is_allpo=0
        if is_allpo:
            return sum(A)
        if is_allne:
            return max(A)
        sum1,temp1=0,maxsum(A)
        for i in range(n):
            sum1+=A[i]
            A[i]=-A[i]
        return max(temp1,sum1+maxsum(A))
