import math
class Solution:
    def minSteps(self, n):
        if n==1:
            return 0
        factor=2
        while n%factor!=0:
            factor+=1
        if factor==n:
            return n
        else:
            return int(self.minSteps(int(n/factor))+factor)

solution=Solution()
num=18
print(solution.minSteps(num))
