class Solution(object):    def checkRecord(self, s):        """        :type s: str        :rtype: bool        """        n=len(s)        if n==0:            return True        countA=0        for i in range(n):            if s[i]=='A':                countA+=1                if countA>1:                    return False            if s[i]=='L':                if i+2<n:                    if s[i+1]=='L' and s[i+2]=='L':                        return False                else:                    return True        return TrueA = "cb"B = "ba"s=Solution()print(s.buddyStrings(A,B))