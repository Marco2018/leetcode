class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class Solution(object):
    def isBST(self,root):
        # Code here
        def getarray(nums, root):
            if root.left:
                getarray(nums, root.left)
            nums.append(root.data)
            if root.right:
                getarray(nums, root.right)
            return

        if not root:
            return True
        nums = []
        getarray(nums, root)
        if len(nums) <= 1:
            return True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return False
        return True
s1=Solution()
root=Node(10)
root.left=Node(7)
root.left.right=Node(11)
root.right=Node(39)
print(s1.isBST(root))
# Python program to check if a binary tree is bst or not 
  
INT_MAX = 4294967296
INT_MIN = -4294967296
  
# A binary tree node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
  
# Returns true if the given tree is a binary search tree 
# (efficient version) 
def isBST(node): 
    return (isBSTUtil(node, INT_MIN, INT_MAX)) 
  
# Retusn true if the given tree is a BST and its values 
# >= min and <= max 
def isBSTUtil(node, mini, maxi): 
      
    # An empty tree is BST 
    if node is None: 
        return True
  
    # False if this node violates min/max constraint 
    if node.data < mini or node.data > maxi: 
        return False
  
    # Otherwise check the subtrees recursively 
    # tightening the min or max constraint 
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi)) 
  
# Driver program to test above function 
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if (isBST(root)): 
    print "Is BST"
else: 
    print "Not a BST"