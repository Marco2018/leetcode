class Solution:
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        stack=[]
        dict={')':'(',']':'[','}':'{'}
        for i in range(n):
            if s[i] in dict:
                if len(stack)==0:
                    return False
                elif stack[-1]==dict[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack)==0:
            return  True
        else:
            return False
s ="{[]}"
print(Solution.isValid(s))