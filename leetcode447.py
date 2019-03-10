class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count=0
        for j in range(len(points)):
            dict={}
            for i in range(len(points)):
                dis=(points[j][0]-points[i][0])**2+(points[j][1]-points[i][1])**2
                if dis not in dict:
                    dict[dis]=1
                else:
                    dict[dis]+=1
            for key,value in dict.items():
                count+=value*(value-1)
        return count
solution=Solution()
points=[[0,0],[1,0],[2,0]]
print(solution.numberOfBoomerangs(points))




