class Solution(object):    def computeArea(self, A, B, C, D, E, F, G, H):        """        :type A: int        :type B: int        :type C: int        :type D: int        :type E: int        :type F: int        :type G: int        :type H: int        :rtype: int        """        area = max(0, (C-A)*(D-B)) + max(0, (G-E)*(H-F))        a, b = max(A, E), max(B, F)        c, d = min(C, G), min(D, H)        overlap = max(0, (c-a)) * max(0, (d-b))        return area - overlap