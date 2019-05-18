class Solution:
    def isMatch(self, s,p):
        dp=[[False]*(len(s)+1) for i in range(len(p)+1)]
        dp[0][0]=True
        # update then s is empty and p is not
        for i in range(2,len(p)+1):
            dp[i][0]=dp[i-2][0] and p[i-1]=='*'

        for i in range(1,len(p)+1):
            for j in range(1,len(s)+1):
                # not *
                if p[i-1]!="*":
                    dp[i][j]=dp[i-1][j-1] and (p[i-1]==s[j-1] or p[i-1]=='.')
                # p[i-1]=="*"
                else:
                    # eliminate: *  stands for 0 char or 1 char
                    dp[i][j]=dp[i-2][j] or dp[i-1][j]
                    if p[i-2]==s[j-1] or p[i-2]=='.':
                        # if p[i-2] the char before "*" ==s[j-1],dp[i][j]=dp[i][j] or dp[i][j-1]: use * to represent s[i-1] char
                        dp[i][j]=dp[i][j] or dp[i][j-1]
        return dp[len(p)][len(s)]