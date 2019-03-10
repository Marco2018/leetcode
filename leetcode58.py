class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        b=list(s)
        b.reverse()
        count=0
        isfirst=0
        for i in range(len(s)):
            if b[i]!=" ":
                isfirst=1
                count += 1
            if b[i]==" " and isfirst==1:
                break
        return count
object1=Solution()
s="   a  "
print(Solution.lengthOfLastWord(object1,s))