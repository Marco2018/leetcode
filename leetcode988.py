# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:             
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        if root==None:
            return ""
        left=self.smallestFromLeaf(root.left)
        right=self.smallestFromLeaf(root.right)
        if right=="" or (left!="" and left<right):
            return left+chr(97+root.val)
        else:
            return right+chr(97+root.val)