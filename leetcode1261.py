class FindElements:

    def __init__(self, root: TreeNode):
        if not root:
            return
        self.nums = set()
        self.root = self.build(root, 0)
        return

    def build(self, root, val):
        if not root:
            return
        root.val = val
        self.nums.add(val)
        root.left = self.build(root.left, val*2+1)
        root.right = self.build(root.right, val*2+2)
        return root

    def find(self, target: int) -> bool:
        if target in self.nums:
            return True
        return False