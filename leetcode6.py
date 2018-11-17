from collections import defaultdict
class Solution:
    def convert(self, s, numRows):
        if len(s)<=1 or numRows<=1:
            return s
        n=2*numRows-2
        dict1=defaultdict(list)
        for i in range(len(s)):
            j=i%n
            if j<numRows:
                dict1[j].append(s[i])
            else:
                j-=numRows
                dict1[numRows-2-j].append(s[i])
        string=""
        for i in range(numRows):
            for char in dict1[i]:
                string+=char
        return string
s1=Solution()
print(s1.convert("PAYPALISHIRING",1))