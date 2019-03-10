class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        if preorder==[]:
            return None
        node=TreeNode(preorder[0])
        if len(preorder)==1:
            return node
        for i in range(1,len(preorder)):
            if preorder[i]>preorder[0]:
                break
        if preorder[-1]<preorder[0]:
            i+=1
        node.left=self.bstFromPreorder(preorder[1:i])
        node.right=self.bstFromPreorder(preorder[i:])
        return node
s1=Solution()
res=s1.bstFromPreorder([4,2])
print(res)
