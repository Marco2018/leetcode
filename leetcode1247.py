class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        x1, y1 = 0, 0
        res = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    x1 += 1
                else:
                    y1 += 1
        if (x1+y1)%2 == 1:
            return -1
        res += int(x1/2) + int(y1/2)
        res += x1%2 +y1%2
        return res
        
""" xx, yy needs one swap, and xy yx needs two swaps, so find the pair of x and the number of redundant x"""