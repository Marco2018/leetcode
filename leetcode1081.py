class Solution:
    def smallestSubsequence(self, text):
        dict = {}
        for i, c in enumerate(text):
            dict[c] = i
        stack = []
        for i,c in enumerate(text):
            if c in stack: continue
            while stack and stack[-1] > c and i < dict[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)