class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        if n==1:
            return [[1]]
        if n==2:
            return [[1],[1,1]]
        res=[[1],[1,1]]
        for i in range(2,n):
            line=[1]
            for j in range(1,i):
                temp=res[i-1][j]+res[i-1][j-1]
                line.append(temp)
            line.append(1)
            res.append(line)
        return res
object1=Solution()
n=5
print(Solution.generate(object1,n))