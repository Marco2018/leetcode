class Solution(object):    def toLowerCase(self, str):        """        :type str: str        :rtype: str        """        return str.lower()s = Solution()M=[[1,1,0], [1,1,1], [0,1,1]]print(s.findCircleNum(M))