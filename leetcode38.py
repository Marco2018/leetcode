class Solution:
    def countsay(self,str1):
        ans=""
        count=1
        for i in range(len(str1)):
            if i<len(str1)-1:
                if str1[i]==str1[i+1]:
                    count=count+1
                else:
                    ans=ans+str(count)+str1[i]
                    count=1
            else:
                ans = ans + str(count) + str1[i]
        return ans

    def countAndSay(self,n):
        """
        :type n: int
        :rtype: str
        """
        str1="1"
        for i in range(1,n):
            str1=self.countsay(str1)
        return str1

object1=Solution()
print(Solution.countAndSay(object1,6))