class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
class Solution(object):

    def balancedtree(self,root):
        def get_height(root):
            if not root:
                return 0
            else:
                left=root.left
                return max(get_height(root.left),get_height(root.right))+1
        if not root:
            return True
        left=get_height(root.left)
        right=get_height(root.right)
        if abs(left-right)>1:
            return False
        else:
            return self.balancedtree(root.left) and self.balancedtree(root.right)
s1=Solution()
root=Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.right=Node(4)
print(s1.balancedtree(root))