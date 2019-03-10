class Solution:
    def largestSumAfterKNegations(self, A,K):
        A.sort()
        A2=[abs(x) for x in A]
        A2.sort()
        i,n=0,len(A)
        while i<n and A[i]<=0 and i<K:
            A[i]=-A[i]
            i += 1
        min_num=A2[0]
        if K>i:
            if (K-i)%2==1:
                return sum(A)-2*min_num
            else:
                return sum(A)
        else:
            return sum(A)

s1=Solution()
res=s1.largestSumAfterKNegations([4,2,3],1)
print(res)
