# Definition for a binary tree node.# class TreeNode(object):#     def __init__(self, x):#         self.val = x#         self.left = None#         self.right = Noneclass Solution(object):    def isSameTree(self, p, q):        """        :type p: TreeNode        :type q: TreeNode        :rtype: bool        """        if p==None and q==None:            return True        elif (p==None and q!=None) or(p!=None and q==None):            return False        elif p.val!=q.val:            return False        else:            return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))#trees=Solution()print(s.ladderLength(beginWord,endWord,wordList))Given two binary trees, write a function to check if they are the same or not.Two binary trees are considered the same if they are structurally identical and the nodes have the same value.