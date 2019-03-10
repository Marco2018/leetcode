class Node:
    def __init__(self,value):
        self.left=None
        self.val=value
        self.right=None
class Solution(object):
    def lca(self,root,a,b):
        if not root:
            return
        if root.val==a or root.val==b:
            return root.val
        else:
            left=self.lca(root.left,a,b)
            right=self.lca(root.right,a,b)
            if left and right:
                return root.val
            else:
                if left:
                    return left
                else:
                    return right
s1=Solution()
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
a,b=4,5
print(s1.lca(root,a,b))