class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N<=1:return 1-N
        temp=1
        while temp<=N:
            temp*=2
        return temp-N-1
s1=Solution()
str=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s1.gameOfLife(str)
print(str)
