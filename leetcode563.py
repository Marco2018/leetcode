from collections import dequeclass Node:    def __init__(self,val):        self.l=None        self.r=None        self.v=valclass Tree:    def __init__(self):        self.root=None    def getRoot(self):        return self.root    def add(self, val):        if (self.root == None):            self.root = Node(val)        else:            self._add(val, self.root)    def _add(self, val, node):        if (val < node.v):            if node.l != None:                self._add(val, node.l)            else:                node.l = Node(val)        else:            if node.r != None:                self._add(val, node.r)            else:                node.r = Node(val)    def find(self,val):        if(self.root!=None):            return self._find(val,self.root)        else:            return None    def _find(self,val,node):        if val==node.v:            return node        elif val<node.v:            if node.l!=None:                self._find(val,node.l)            else:                print("no exist")        elif val>node.v:            if node.r!=None:                self._find(val,node.r)            else:                print("no exist")    def deleteTree(self):        self.root=None    def printTree(self):        if self.root!=None:            self._printTree(self.root)    def _printTree(self,node):        if node!=None:            self._printTree(node.l)            print(" "+str(node.v)+" ")            self._printTree(node.r)    def add2(self, num):        if num==-1:            node=None        else:            node = Node(num)        if self.root is None:            self.root = node        else:            q = [self.root]            while True:                pop_node = q.pop(0)                if pop_node.l is None:                    pop_node.l = node                    return                elif pop_node.r is None:                    pop_node.r = node                    return                else:                    q.append(pop_node.l)                    q.append(pop_node.r)# Definition for a binary tree node.# class TreeNode(object):#     def __init__(self, x):#         self.val = x#         self.left = None#         self.right = None# Definition for a binary tree node.# class TreeNode(object):#     def __init__(self, x):#         self.val = x#         self.left = None#         self.right = None# Definition for a binary tree node.# class TreeNode(object):#     def __init__(self, x):#         self.val = x#         self.left = None#         self.right = None# Definition for a binary tree node.# class TreeNode(object):#     def __init__(self, x):#         self.val = x#         self.left = None#         self.right = Noneclass Solution(object):    def findTilt(self, root):        """        :type root: TreeNode        :rtype: int        """        def gettile(root,alltiles):            if root==None:                return 0,0,alltiles            leftsum,tile,alltiles=gettile(root.l,alltiles)            rightsum,tile2,alltiles=gettile(root.r,alltiles)            alltiles.append(tile)            alltiles.append(tile2)            return leftsum+root.v+rightsum,abs(leftsum-rightsum),alltiles        alltiles=[]        sum1,tile,alltiles=gettile(root,alltiles)        alltiles.append(tile)        return sum(alltiles)s=Solution()tree = Tree()nums=[1,2,2,3,4,4,3]tree.add2(1)tree.add2(2)tree.add2(3)tree.printTree()root=tree.getRoot()print(s.findTilt(root))#tree"""tree = Tree()tree.add(3)tree.add(4)tree.add(0)tree.add(8)tree.add(2)tree.printTree()print ((tree.find(3)).v)print (tree.find(10))tree.deleteTree()tree.printTree()""""""class Solution(object):    def isSymmetric(self, root):        def issame(root1,root2):            if root1.val!=root2.val:                return False            else:                return issame(root1.left,root2.right) and issame(root1.right,root2.left)        if root==None:            return True        return issame(root.left,root.right)"""