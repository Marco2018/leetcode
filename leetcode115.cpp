#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<sstream>
using namespace std;
// for dp
class Solution {
public:
	int numDistinct(string s, string t) {
		int n1 = s.size(), n2 = t.size();
		if (n1 == 0 && n2 != 0) return 0;
		int i,j;
		vector<vector <int> > dp(n1+1, vector<int>(n2+1, 0));
		for (i = 0; i < n1 + 1; i++) {
			dp[i][0] = 1;
		}
		for (i = 1; i < n1 + 1; i++) {
			for (j = 1; j <= min(i,n2); j++) {
				if (s[i-1] == t[j-1]) {
					dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
				}
				else
					dp[i][j] = dp[i - 1][j];
			}
		}
		return dp[n1][n2];
	}
};
int main() {
	Solution s1 = Solution();
	int res=s1.numDistinct("babgbag", "bag");
	cout << res;
	system("pause");
	return 0;
}