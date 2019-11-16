2019 Google Kickstart Round B Solution
A. Building Palindromes
给一个长度为N的字符串以及Q次询问，每次询问字符串区间[Li,Ri]中的字符能否重构成一个回文串。N,Q≤105
签到题，字符串中只有大写字母，就存一下第i位之前每个字母的数量，然后计算区间内字母数量能否构成回文就AC了

#include<bits/stdc++.h>
using namespace std;
int t;
int n,m;
int dp[100005][26];
string str;
int ans;
int main()
{
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
       scanf("%d%d",&n,&m);
       ans=0;
       cin>>str;
       memset(dp,0,sizeof(dp));
       for(int i=1;i<=n;i++)
       {
           for(int j=0;j<26;j++)
           {
               if(str[i-1]-'A'==j)
                   dp[i][j]=dp[i-1][j]+1;
               else dp[i][j]=dp[i-1][j];
           }
       }
       for(int i=1;i<=m;i++)
       {
           int l,r;
           scanf("%d%d",&l,&r);
           int falg=0;
           for(int j=0;j<26&&falg<3;j++)
           {
               //cout<<dp[r][j]-dp[l-1][j]<<endl;
               if((dp[r][j]-dp[l-1][j])%2)
               {
                   falg++;
               }
           }
           if(falg<2) ans++;
       }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}