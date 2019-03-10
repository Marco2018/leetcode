class Solution:
    def findTheDifference(self, s, t):
        n=len(s)
        dict1={}
        dict2={}
        for i in range(0,n):
            if s[i] in dict1:
                dict1[s[i]]=dict1[s[i]]+1
            else:
                dict1[s[i]]=1
        for i in range(0,n+1):
            if t[i] in dict2:
                dict2[t[i]]=dict2[t[i]]+1
            else:
                dict2[t[i]]=1
        for item in dict2:
            if item not in dict1:
                return item
            elif dict1[item]!=dict2[item]:
                return item

object1=Solution()
s="abcd"
t="abcde"
print(Solution.findTheDifference(object1,s,t))