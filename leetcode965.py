class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.nums = []

        def helper(root):
            if root.left:
                helper(root.left)
            self.nums.append(root.val)
            if root.right:
                helper(root.right)
            return

        if root == None:
            return True
        helper(root)
        temp = self.nums[0]
        for i in range(1, len(self.nums), 1):
            if self.nums[i] != temp:
                return False
        return True
