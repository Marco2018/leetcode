class Solution:
    def upper_bound(self, nums, target):
        left, right = 0, len(nums)-1
        while left < right:
            mid = int((left+right)/2)
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    def reverseParentheses(self, s):
        n= len(s)
        lefts, rights, chars = [], [], []
        for i in range(n):
            if s[i] == "(":
                lefts.append(i)
            elif s[i] == ")":
                rights.append(i)
            chars.append(s[i])
        while len(lefts) and len(rights):
            left = lefts.pop()
            index = self.upper_bound(rights, left)
            right = rights[index]
            del rights[index]
            chars[left+1:right] = chars[left+1:right][::-1]
        res = ""
        for i in range(n):
            if chars[i]!="(" and chars[i]!=")":
                res+=chars[i]
        return res