#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<sstream>
using namespace std;
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {};
};
class Solution {
public:
	string getPermutation(int n, int k) {
		vector<int> nums(n);
		stringstream ss;
		for (int i = 0; i < n; i++) {
			nums[i] = i + 1;
		}

		while (--k) {
			next_permutation(nums.begin(), nums.end());
		}
		for (int i = 0; i < n; i++) {
			ss << nums[i];
		}
		string str = ss.str();
		return str;
	}
};
int main() {
	string nu;
	Solution s1 = Solution();
	int n = 3, k = 3;
	nu=s1.getPermutation(n,k);
	cout << nu;
	system("pause");
	return 0;
}