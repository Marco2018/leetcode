class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s,t=[],[]
        count,count2=0,0
        for i in range(len(S)-1,-1,-1):
            if S[i]=="#":
                count+=1
                continue
            else:
                if count<=0:
                    s.append(S[i])
                else:
                    count-=1
        for j in range(len(T)-1,-1,-1):
            if T[j]=="#":
                count2+=1
                continue
            else:
                if count2<=0:
                    t.append(T[j])
                else:
                    count2-=1
        if s==t:
            return True
        else:
            return False
solution=Solution()
S = "ab#c"
T = "ad#c"
print(solution.backspaceCompare(S,T))
