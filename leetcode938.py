# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        def helper(root, L, R):
            if L <= root.val <= R:
                self.res += root.val
            if root.left and root.val > L:
                helper(root.left, L, R)
            if root.right and root.val < R:
                helper(root.right, L, R)
            return

        self.res = 0
        if not root:
            return 0
        helper(root, L, R)
        return self.res
