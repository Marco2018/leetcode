# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root):
        if not root:
            return 0
        level = collections.deque()
        level.append(root)
        max_sum, index = -float("inf"), -1
        step = 0
        while level:
            step += 1
            tmp_sum = 0
            for i in range(len(level)):
                node = level.popleft()
                tmp_sum += node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if max_sum < tmp_sum:
                max_sum, index = tmp_sum, step
        return index
        