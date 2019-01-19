# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxPathSum(self, root):
        self.res=-float("inf")
        def helper(root):
            if not root:
                return 0
            left=helper(root.left)
            right=helper(root.right)
            if left<0: left=0
            if right<0: right=0
            self.res=max(self.res,root.val+left+right)
            return root.val+max(left,right)
        helper(root)
        return self.res
s1=Solution()
root=TreeNode(-10)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
print(s1.maxPathSum(root))