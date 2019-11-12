import numpy as np
class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        nums = np.zeros((n, m))
        for r,c in indices:
            nums[r] = 1-nums[r]
            nums[:,c] = 1-nums[:,c]
        return int(sum(sum(nums)))
            
        