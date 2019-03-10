#include <iostream>
#include <array>
#include <vector>
#include <stack>
using namespace std;
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
	void flatten(TreeNode* root) {
		if (root == NULL) return;
		stack<TreeNode*> stack1;
		TreeNode* temp = root;
		stack1.push(root);
		while (!stack1.empty()) {
			TreeNode* cur = stack1.top();
			stack1.pop();
			if (cur->right != NULL) {
				stack1.push(cur->right);
			}
			if (cur->left!=NULL) {
				stack1.push(cur->left);
			}
			if (!stack1.empty()) {
				cur->right = stack1.top();
			}
			cur->left = NULL;
		}
	}
};
int main() {
	Solution s1;
	TreeNode* root;
	root = new TreeNode(1);
	root->left=new TreeNode(2);
	root->right = new TreeNode(3);
	s1.flatten(root);
	system("pause");
	return 0;
}