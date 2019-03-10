class Solution:
    def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            return 0
        else:
            return haystack.find(needle)


haystack = "hello"
needle = "ll"
print(Solution.strStr(haystack,needle))