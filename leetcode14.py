class Solution(object):
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0 or len(strs[0]) == 0: return ""
        for j in range(1, len(strs[0]) + 2):
            for i in range(1, n):
                if len(strs[i]) < j:
                    return strs[0][:j - 1]
                if strs[i][:j] != strs[0][:j]:
                    return strs[0][:j - 1]
        return strs[0][:j - 1]

Runtime: 20 ms, faster than 93.94% of Python online submissions for Longest Common Prefix.
找到最短的str
shortest = min(strs, key=len)  “flow”