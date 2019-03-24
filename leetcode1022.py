class Solution:
    def smallestRepunitDivByK(self, K):
        if K==1:return 1
        yu,seen,count=0,set(),0
        while True:
            yu=(10*yu+1)%K
            count+=1
            if yu==0:
                return count
            if yu in seen:
                return -1
            else:
                seen.add(yu)
s1=Solution()
res=s1.smallestRepunitDivByK(95)
print(res)