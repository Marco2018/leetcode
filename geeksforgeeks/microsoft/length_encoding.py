class Node:
    def __init__(self,value):
        self.left=None
        self.val=value
        self.right=None
class Solution(object):
    def length_encoding(self,s):
        n=len(s)
        if n==0:
            return ""
        res,char,count="",s[0],1
        for i in range(1,n):
            if s[i]!=char:
                res+=(char+str(count))
                count,char=1,s[i]
                continue
            else:
                count+=1
        if count!=0:
            res+=(char+str(count))
        return res
s1=Solution()
print(s1.length_encoding("wwwwaaadexxxxx"))