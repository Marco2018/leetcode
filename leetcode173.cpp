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
/**
* Definition for binary tree
* struct TreeNode {
*     int val;
*     TreeNode *left;
*     TreeNode *right;
*     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
* };
*/
class BSTIterator {
public:
	void helper(TreeNode *root) {
		if (root->left != NULL)
			helper(root->left);
		nums.push_back(root->val);
		if (root->right != NULL)
			helper(root->right);
	}
	BSTIterator(TreeNode *root) {
		if (root != NULL) {
			helper(root);
		}
		n = nums.size();
	}

	/** @return whether we have a next smallest number */
	bool hasNext() {
		if (n>i)
			return true;
		return false;
	}

	/** @return the next smallest number */
	int next() {
		return nums[i++];
	}
private:
	vector<int>nums;
	int i = 0, n;
};

/**
* Your BSTIterator will be called like this:
* BSTIterator i = BSTIterator(root);
* while (i.hasNext()) cout << i.next();
*/
int main() {
	string nu;
	Solution s1 = Solution();
	int n = 3, k = 3;
	nu=s1.getPermutation(n,k);
	cout << nu;
	system("pause");
	return 0;
}