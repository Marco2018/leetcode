class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans=[]
        def dfs(S,pos,str):
            if pos==len(S):
                ans.append(str)
                return
            else:
                if S[pos].isalpha():
                    dfs(S,pos+1,str+S[pos].upper())
                    dfs(S, pos + 1, str + S[pos].lower())
                else:
                    dfs(S,pos+1,str+S[pos])
        dfs(S,0,"")
        return ans

solution=Solution()
s="a1b2"
print(solution.letterCasePermutation(s))



