import numpy
class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if wall==[]:
            return 0
        wall2=[]
        for i in range(len(wall)):
            wall2.append(numpy.add.accumulate(wall[i]))
        dict={}
        for i in range(len(wall2)):
            for j in range(len(wall2[i])-1):
                if wall2[i][j] not in dict:
                    dict[wall2[i][j]]=1
                else:
                    dict[wall2[i][j]]+=1
        if dict=={}:
            return len(wall)
        else:
            return len(wall)-max(dict.values())
solution=Solution()
wall=[[1],[1],[1]]
print(solution.leastBricks(wall))
