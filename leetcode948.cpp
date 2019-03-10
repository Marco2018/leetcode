#include <iostream>
#include <array>
#include <vector>
#include <stack>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
	int bagOfTokensScore(vector<int>& tokens, int P) {
		int max_tokens = 0, temp_tokens = 0;
		sort(tokens.begin(), tokens.end());
		int i= 0,j= tokens.size() - 1;
		while (j>=i) {
			while (j>=i && P >= tokens[i]) {
				P -= tokens[i++];
				temp_tokens++;
				max_tokens = max(max_tokens, temp_tokens);
			}
			if (j >= i && temp_tokens>0) {
				P += tokens[j--];
				temp_tokens--;
			}
			else {
				break;
			}
		}
		return max_tokens;
	}
};
int main() {
	Solution s1;
	vector<int> nums = {26};
	int P = 51;
	int res=s1.bagOfTokensScore(nums,P);
	cout << res;
	system("pause");
	return 0;
}
// for this kind problem, simulate stack