class Solution:
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res=float("inf")
        n=len(points)
        if n<=3: return 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    [x1,y1]=points[i][0],points[i][1]
                    [x2, y2] = points[j][0], points[j][1]
                    [x3, y3] = points[k][0], points[k][1]
                    if [x2+x3-x1,y2+y3-y1] in points:
                        vec1=[x2-x1,y2-y1]
                        vec2=[x3-x1,y3-y1]
                        if vec1[0]*vec2[0]+vec1[1]*vec2[1]==0:
                            res=min(res,(vec1[0]*vec1[0]+vec1[1]*vec1[1])**0.5*(vec2[0]*vec2[0]+vec2[1]*vec2[1])**0.5)
        return res
s1=Solution()
print(s1.minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]]))

"""
        n=len(A)
        if n==0:
            return 0
        if A[n-1]>=A[0]:
            return n-1
        else:
            return max(self.maxWidthRamp(A[1:]),self.maxWidthRamp(A[:n-1]))
        TLE
"""
