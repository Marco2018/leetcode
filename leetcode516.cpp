#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
class Solution {
public:
    int max(int a,int b){
        if (a>b) return a;
        else return b;
    }
    int longestPalindromeSubseq(string s) {
        int n=s.size();
        int dp[n][n];
        fill(dp[0], dp[0]+n*n, 0);
        for(int i=n-1;i>=0;i--){
            dp[i][i]=1;
            for (int j=i+1;j<n;j++){
                if (s[i]==s[j])dp[i][j]=dp[i+1][j-1]+2;
                else dp[i][j]=max(dp[i+1][j],dp[i][j-1]);
            }
        }
        return dp[0][n-1];
    }
};
int main() {
    string str="cbbd";
    Solution s;
    printf("%d",s.longestPalindromeSubseq(str));
    return 0;
}
State transition:
dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
otherwise, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])

        还要注意这题 i的顺序从n-1开始
