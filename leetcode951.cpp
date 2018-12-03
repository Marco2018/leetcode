#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<sstream>
using namespace std;
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	
};
class Solution {
public:
	bool flipEquiv(TreeNode* root1, TreeNode* root2) {
		if (root1 == NULL && root2 == NULL) return true;
		else {
			if (root1 == NULL || root2 == NULL) return false;
		}
		if (root1->val != root2->val) return false;
		else {
			bool index1, index2,index11,index12,index21,index22;
			index11 = flipEquiv(root1->left, root2->left);
			index12 = flipEquiv(root1->right, root2->right);
			index1 = index11 && index12;

			index22 = flipEquiv(root1->right, root2->left);
			index21 = flipEquiv(root1->left, root2->right);
			index2 = index21 && index22;
			return index1 || index2;
		}
	}
};
int main() {
	Solution s1 = Solution();
	vector<int> nums = { 1,2 };
	bool res;
	TreeNode* T = new TreeNode(1);
	T->left = new TreeNode(2);
	T->left->left = new TreeNode(4);
	T->left->right = new TreeNode(5);
	T->right = new TreeNode(3);
	T->right->left = new TreeNode(6);
	T->left->right->left = new TreeNode(7);
	T->left->right->right = new TreeNode(8);

	TreeNode* T1 = new TreeNode(1);
	T1->left = new TreeNode(3);
	T1->left->right = new TreeNode(6);
	T1->right = new TreeNode(2);
	T1->right->left = new TreeNode(4);
	T1->right->right = new TreeNode(5);
	T1->right->right->left = new TreeNode(8);
	T1->right->right->right = new TreeNode(7);
	res= s1.flipEquiv(T,T1);
	cout << res;
	system("pause");
	return 0;
}