class Solution:    def minAddToMakeValid(self, S):        """        :type S: str        :rtype: int        """        n,count,temp=len(S),0,0        if n==0:            return 0        for i in range(n):            if S[i]=="(":                temp+=1            if S[i]==")":                if temp>0:                    temp-=1                else:                    count+=1        if temp>0:            count+=temp        return count