class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0:
            num=-num
        if num==0 or num==1:
            return True
        while num%2==0:
            num/=2
        while num%3==0:
            num/=3
        while num%5==0:
            num/=5
        if num==1:
            return True
        else:
            return False

solution=Solution()
num=-2147483648
print(solution.isUgly(num))
