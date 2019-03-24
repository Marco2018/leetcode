class Solution:
    def canThreePartsEqualSum(self, A):
        sum1=sum(A)
        if sum1%3!=0:return False
        else:target=sum1//3
        count,temp=0,0
        for i in range(len(A)):
            temp+=A[i]
            if temp==target:
                temp=0
                count+=1
        if count>=3:
            return True
        return False
s1=Solution()
res=s1.smallestRepunitDivByK(95)
print(res)