class Solution(object):
    def removeduplicate(self,s):
        res=""
        for i in range(len(s)):
            if s[i] not in res:
                res+=s[i]
        return res

s1=Solution()
s="geeksforgeeks"
print(s1.removeduplicate(s))