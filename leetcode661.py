class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows,cols=len(M),len(M[0])
        def getgray(i,j,M):
            value,count=0,0
            for ii in range(-1,2):
                for jj in range(-1,2):
                    a,b=i+ii,j+jj
                    if -1<a<len(M) and -1<b<len(M[0]):
                        count+=1
                        value+=M[a][b]
            return int(value/count)
        M1=[[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                M1[i][j]=getgray(i,j,M)
        return M1

solution=Solution()
input=[[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
print(solution.imageSmoother(input))



