class Solution:    def searchMatrix(self, matrix, target):        """        :type matrix: List[List[int]]        :type target: int        :rtype: bool        """        for item in matrix:            if target in item:                return True        return Falses=Solution()matrix = [[1,2,3],[3,4,5]]target=3print(s.searchMatrix(matrix,target))