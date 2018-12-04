#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {};
};
class Solution {
public:
	vector<int> nums;
	void helper(TreeNode* root) {
		nums.push_back(root->val);
		if (root->left)
			helper(root->left);
		if (root->right)
			helper(root->right);
	}
	vector<int> findMode(TreeNode* root) {
		vector<int> res;
		if (root == NULL) return res;
		helper(root);
		map<int, int> mp;
		int max_num = 0;
		for (int& a : nums) {
			mp[a]++;
			max_num = max(max_num, mp[a]);
		}
		map<int, int>::iterator ite1;
		for (ite1 = mp.begin(); ite1 != mp.end(); ite1++) {
			if(max_num== ite1->second)
				res.push_back(ite1->first);
		}
		return res;
	}
};
using namespace std;
int main() {
	vector<int> nu;
	Solution s1 = Solution();
	TreeNode* T = new TreeNode(2147483647);
	//T->left= new  TreeNode(3);
	//T->left->left = new TreeNode(3);
	nu=s1.findMode(T);
	cout << nu[0];
	system("pause");
	return 0;
}