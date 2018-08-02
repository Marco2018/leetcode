class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sumdigits(str):
            sum=0
            for i in range(len(str)):
                sum+=int(str[i])**2
            return sum
        for i in range(1000):
            n=sumdigits(str(n))
            if n==1:
                return True
        return False

solution=Solution()
num=19
print(solution.isHappy(num))
