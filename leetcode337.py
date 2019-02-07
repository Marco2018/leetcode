# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob_skip(root):
            if not root:
                return 0,0
            rob_left,skip_left=rob_skip(root.left)
            rob_right,skip_right=rob_skip(root.right)
            rob=root.val+skip_left+skip_right
            skip = max(rob_left, skip_left) + max(rob_right, skip_right)
            return rob,skip
        return max(rob_skip(root))
s1=Solution()
root=TreeNode(3)
print(s1.rob(root))
