class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            if a == 0: return b
            return gcd(b % a, a)
        d = gcd(len(str2), len(str1))
        if str2[:d]*int(len(str2)/d)==str2 and str2[:d]*int(len(str1)/d)==str1:
            return str2[:d]
        return ""
        