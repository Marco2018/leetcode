class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        n=len(S)
        letters,ans=[],""
        for i in range(n):
            if S[i].isalpha():
                letters.append(S[i])
        letters.reverse()
        j=0
        for i in range(n):
            if S[i].isalpha():
                ans+=letters[j]
                j+=1
            else:
                ans+=S[i]
        return ans