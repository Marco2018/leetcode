class Solution:    def convertToBase7(self, num):        """        :type num: int        :rtype: str        """        if num==0:            return "0"        ans=[]        index=0        if num<0:            index=1            num=-num        while num:            yu=num%7            ans.append(str(yu))            num=int((num-yu)/7)        if index:            ans.append("-")        ans.reverse()        return "".join(i for i in ans)s=Solution()num=0print(s.convertToBase7(num))