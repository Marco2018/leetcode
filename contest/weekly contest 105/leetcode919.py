# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        root = self.root
        level1, level2 = deque(), deque()
        level1.append(root)
        while level1 or level2:
            while level1:
                temp = level1[0]
                level1.popleft()
                if temp.left == None:
                    temp.left = TreeNode(v)
                    return temp.val
                else:
                    level2.append(temp.left)
                if temp.right == None:
                    temp.right = TreeNode(v)
                    return temp.val
                else:
                    level2.append(temp.right)
            level1 = level2.copy()
            level2.clear()

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()