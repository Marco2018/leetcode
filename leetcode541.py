class Solution(object):    def reverseStr(self, s, k):        """        :type s: str        :type k: int        :rtype: str        """        n=len(s)        list1=list(s)        for i in range(0,n,2*k):            list1[i:i+k]=reversed(list1[i:i+k])        return "".join(i for i in list1)s = Solution()str="abcdefg"k=2print(s.reverseStr(str,k))