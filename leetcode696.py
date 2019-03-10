class Solution:
    def countBinarySubstrings(self, s):
        counts=[]
        count=1
        ans=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                counts.append(count)
                count=1
                i+=1
        counts.append(count)
        for j in range(1,len(counts)):
            ans+=min(counts[j-1],counts[j])
        return ans

solution=Solution()
str="10101"
print(solution.countBinarySubstrings(str))
