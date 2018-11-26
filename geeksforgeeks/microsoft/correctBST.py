class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
class Solution(object):
    def correctBST(self,root):
        def get_nums(root):
            if not root:
                return
            if root.left:
                get_nums(root.left)
            self.nums.append(root.val)
            if root.right:
                get_nums(root.right)
        if not root:
            return
        def correct(root):
            if not root:
                return
            if root.left:
                correct(root.left)
            root.val=self.nums[self.count]
            self.count+=1
            if root.right:
                correct(root.right)
        self.nums,self.count=[],0
        get_nums(root)
        n=len(self.nums)
        if n<=1:
            return
        for i in range(1,n):
            if self.nums[i-1]>self.nums[i]:
                index1=i-1
                break
        for i in range(n-2,-1,-1):
            if self.nums[i+1]<self.nums[i]:
                index2=i+1
                break
        self.nums[index1],self.nums[index2]=self.nums[index2],self.nums[index1]
        correct(root)
        return
s1=Solution()
root=Node(10)
root.left=Node(5)
root.left.left=Node(2)
root.left.right=Node(20)
root.right=Node(8)
print(s1.correctBST(root))