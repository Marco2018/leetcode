class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
            
        n = len(colsum)
        if upper + lower != sum(colsum):
            return []
        res = [[0 for i in range(n)] for j in range(2)]
        for i in range(n):
            if colsum[i] == 2:
                if upper <= 0 or lower <= 0:
                    return []
                res[0][i] = 1
                res[1][i] = 1
                upper -= 1 
                lower -= 1
            elif colsum[i] == 1:
                if upper >= lower:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
        return res
        
        