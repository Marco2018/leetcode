#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <algorithm> 
using namespace std;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	
};
bool cmp(vector<int>& a, vector<int>& b) {
	return a[1] < b[1];
}
class Solution {
public:
	
	void helper(TreeNode* root,int x,int y) {
		if (!root)
			return;
		nums.push_back({ root->val,x,y });
		helper(root->left, x - 1, y - 1);
		helper(root->right, x + 1, y - 1);
		return;
	}
	vector<vector<int>> verticalTraversal(TreeNode* root) {
		vector<vector<int>> res;
		helper(root, 0, 0);
		sort(nums.begin(), nums.end(), cmp);
		if (nums.size() == 0) return res;
		int temp_x = nums[0][1];
		vector<int> temp; temp.push_back(nums[0][0]);
		for (int i = 1; i < nums.size(); i++) {
			if (nums[i][1] == temp_x) {
				temp.push_back(nums[i][0]);
			}
			else {
				res.push_back(temp);
				temp.clear(); temp.push_back(nums[i][0]);
				temp_x = nums[i][1];
			}
		}
		res.push_back(temp);
		return res;
	}
private:
	vector<vector<int>> nums;
};
int main() {
	Solution s1;
	TreeNode* root = new TreeNode(3);
	root->left = new TreeNode(9);
	root->right = new TreeNode(20);
	root->right->left = new TreeNode(15);
	root->right->right = new TreeNode(7);
	s1.verticalTraversal(root);
	return 0;
}