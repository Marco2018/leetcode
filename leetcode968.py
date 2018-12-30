class Solution:
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=0
        def dfs(root):
            if not root:
                return 2
            if not root.left and not root.right:
                return 0
            left,right=dfs(root.left),dfs(root.right)
            if left==0 or right==0:  #child is leaf
                self.res+=1
                return 1
            if left==1 or right==1:
                return 2 #its child has a camera
            return 0 #becomes a leaf
        if root==None:
            return 0
        if dfs(root)==0: #still has a root to camera
            return self.res+1
        return self.res