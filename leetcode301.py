class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res=set()
        def helper_left(s,last_i,last_j):
            count=0
            for i in range(len(s)):
                if s[i] == "(":
                    count -= 1
                elif s[i] == ")":
                    count += 1
                else:
                    continue
                if count <0:
                    for j in range(last_j,i+1):
                        if s[j]=="(":
                            helper_left(s[:j]+s[j+1:],i,j)
                    return
            self.res.add(s[::-1])
        def helper_right(s,last_i,last_j):
            count=0
            for i in range(len(s)):
                if s[i]=="(":
                    count+=1
                elif s[i]==")":
                    count-=1
                else:
                    continue
                if count<0:
                    for j in range(last_j,i+1,1):
                        if s[j]==")":
                            helper_right(s[:j]+s[j+1:],i,j)
                    return
            helper_left(s[::-1],0,0)
        helper_right(s,0,0)
        return list(self.res)

"""
    def removeInvalidParentheses(self, s):
        self.allstr=set()
        def check(str1):
            count=0
            for i in range(len(str1)):
                if str1[i]=="(":
                    count+=1
                if str1[i]==")":
                    count-=1
                if count<0:
                    return False
            if count!=0:
                return False
            return True

        def helper(s,temp):
            if temp not in self.allstr and check(temp):
                self.allstr.add(temp)
            if s!="":
                helper(s[1:], temp + s[0])
                helper(s[1:],temp)
            return
        helper(s,"")
        maxlen=-1
        for item in self.allstr:
            maxlen=max(maxlen,len(item))
        res=[tmp for tmp in self.allstr if len(tmp)==maxlen]
        return res
"""