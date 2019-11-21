from functools import cmp_to_key
class Solution:

    def orderOfLargestPlusSign(self, S, D):
        def issubsequence(item, S):
            i, start = 0, 0
            flag=False
            while i < len(item):
                while start < len(S):
                    if S[start] == item[i]:
                        flag=True
                        break
                    start += 1
                if not flag:return False
                i += 1
                flag=False
            return True

        def cmp(x, y):
            return len(y) - len(x)
        D.sort(key=cmp_to_key(cmp))
        for item in D:
            if issubsequence(item, S):
                return item
        return ""


obj = Solution()
S = "abppplee"
D = ["able", "ale", "apple", "bale", "kangaroo"]
print(obj.orderOfLargestPlusSign(S, D))