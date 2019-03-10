class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]]=1
            else:
                dict[s[i]]+=1
        length=0
        isodd=0
        for key,value in dict.items():
            if value%2==0:
                length+=value
            else:
                isodd=1
                length+=value-1
        length+=isodd
        return length
solution=Solution()
s="AAabccccdd"
print(solution.longestPalindrome(s))




