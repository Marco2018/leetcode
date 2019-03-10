class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        count=1
        ans=[]
        start,end=0,0
        for i in range(1,len(S)):
            if S[i]==S[i-1]:
                count+=1
                end=i
            else:
                if count>=3:
                    ans.append([start,end])
                count=1
                start=i
        if count >= 3:
            ans.append([start, end])
        return ans
solution=Solution()
S="aaa"
print(solution.largeGroupPositions(S))




