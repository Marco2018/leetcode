class Solution:    def isLongPressedName(self, name, typed):        """        :type name: str        :type typed: str        :rtype: bool        """        n1, n2 = len(name), len(typed)        if n1 == 0:            return True        if n1 > n2:            return False        if name[0] != typed[0]:            return False        before, i, j = name[0], 1, 1        while i < n1 and j < n2:            if name[i] == typed[j]:                before = name[i]                j += 1                i += 1            elif typed[j] == before:                j += 1            else:                return False        if i < n1:            return False        return Trues=Solution()graph = [1,0,1,0,1]print(s.threeEqualParts(graph))