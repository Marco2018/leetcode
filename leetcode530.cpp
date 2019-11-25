#include <iostream>
#include <vector>
#include <queue>
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
class Solution {
public:
    void inorderTraverse(TreeNode* root, int& val, int& min_dif) {
        if (root->left != NULL) inorderTraverse(root->left, val, min_dif);
        if (val >= 0) min_dif = min(min_dif, root->val - val);
        val = root->val;
        if (root->right != NULL) inorderTraverse(root->right, val, min_dif);
    }
    int getMinimumDifference(TreeNode* root) {
        auto min_dif = INT_MAX, val = -1;
        inorderTraverse(root, val, min_dif);
        return min_dif;
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
