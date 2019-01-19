import heapq
class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dict1={}
        for i in range(len(points)):
            dict1[(points[i][0],points[i][1])]=points[i][0]**2+points[i][1]**2
        res=heapq.nsmallest(K,points,key=lambda x:dict1[(x[0],x[1])])
        return res

s1=Solution()
print(s1.subarraysDivByK([8,9,7,8,9],8))