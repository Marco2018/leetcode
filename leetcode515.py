# Definition for a binary tree node.class TreeNode:     def __init__(self, x):         self.val = x         self.left = None         self.right = Noneclass Solution:    def largestValues(self, root):        """        :type root: TreeNode        :rtype: List[int]        """        if root==None:            return []        line1,line2,ans=[],[],[]        line1.append(root)        ans.append(root.val)        temp=-float("inf")        while line1 or line2:            while line1:                tmp=line1[-1]                line1.pop()                if tmp.left:                    line2.append(tmp.left)                    temp=max(temp,tmp.left.val)                if tmp.right:                    line2.append(tmp.right)                    temp = max(temp, tmp.right.val)            if temp!= -float("inf"):                ans.append(temp)            temp = -float("inf")            line1=line2.copy()            line2.clear()        return anss=Solution()root=TreeNode(1)root.left=TreeNode(3)root.right=TreeNode(2)root.left.left=TreeNode(5)root.left.right=TreeNode(3)root.right.right=TreeNode(9)print(s.largestValues(root))