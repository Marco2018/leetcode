class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        stack=[-1]
        for i in range(len(s)):
            if stack[-1]!=-1 and s[i]==")" and  s[stack[-1]]=="(":
                stack.pop()
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)
        return max_len
s1=Solution()
print(s1.longestValidParentheses(")()())"))