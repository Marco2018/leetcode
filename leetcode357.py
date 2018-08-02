'''
class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isunique(str):
            dict={}
            for j in range(len(str)):
                if str[j] not in dict:
                    dict[str[j]]=1
                else:
                    return False
            return True
        count=0
        for i in range(10**n):
            if isunique(str(i)):
                count+=1
        return count
'''
class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        if n==1:
            return 10
        count=10
        for i in range(1,n):
            temp=1
            for j in range(i+1):
                if j==0:
                    temp*=9
                else:
                    temp*=(10-j)
            count+=temp
        return count
solution=Solution()
num=1
print(solution.countNumbersWithUniqueDigits(num))
