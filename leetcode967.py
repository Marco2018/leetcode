class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        self.nums=[]
        def helper(path,n):
            if n==N:
                if path not in self.nums:
                    self.nums.append(path)
                return
            if int(path[-1])+K<10:
                temp=int(path[-1])+K
                helper(path+str(temp),n+1)
            if int(path[-1])-K>=0:
                temp=int(path[-1])-K
                helper(path+str(temp),n+1)
        if N==0:
            return []
        if N==1:
            return [0,1,2,3,4,5,6,7,8,9]
        for i in range(1,10,1):
            helper(str(i),1)
        return [int(x) for x in self.nums]