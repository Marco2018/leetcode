class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for x in num:
            while k and stack and stack[-1] > x:
                k -= 1
                stack.pop()
            stack.append(x)
        res = "".join(stack)[:len(stack) - k].lstrip("0")
        if res == "":
            return "0"
        else:
            return res