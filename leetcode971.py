class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        self.next=0
        self.res=[]
        def dfs(root):
            if not root:#如果root到了None 则返回True
                return True
            if root.val!=self.nums[self.next]:
                return False
            else:
                self.next+=1
                if root.left and self.nums[self.next]==root.left.val:##要考虑root.left是否存在
                    return dfs(root.left) and dfs(root.right)
                if root.right and self.nums[self.next]==root.right.val:
                    if root.left:##如果root.left存在还执行到这一步 说明需要flip，否则可能存在left==None的情况
                        self.res.append(root.val)
                    return dfs(root.right) and dfs(root.left)
                return root.left==root.right==None##这边需要判断是已经执行到最后了 返回True 还是在root.left和root.right中都找不到nums[self.next]返回False

        self.nums=voyage
        if dfs(root):
            return self.res
        return [-1]
