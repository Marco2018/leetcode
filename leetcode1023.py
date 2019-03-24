class Solution:
    def get_binary(self,N):
        str1=""
        while N:
            temp=N%2
            str1=str(temp)+str1
            N=N//2
        return str1
    def queryString(self, S, N):
        for i in range(1,N+1):
            str1=self.get_binary(i)
            if str1 not in S:
                return False
        return True
s1=Solution()
res=s1.smallestRepunitDivByK(95)
print(res)