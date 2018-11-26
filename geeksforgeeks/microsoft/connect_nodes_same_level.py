class Node:
    def __init__(self,value):
        self.left=None
        self.val=value
        self.right=None
from collections import deque
class Solution(object):
    def connect_nodes_same_level(self,root):
        if not root:
            return []
        res=[[root.val]]
        line,next_line,next_line_val=deque([root]),deque(),[]
        while len(line)>0:
            for i in range(len(line)):
                if line[i].left:
                    next_line.append(line[i].left)
                    next_line_val.append(line[i].left.val)
                if line[i].right:
                    next_line.append(line[i].right)
                    next_line_val.append(line[i].right.val)
            if next_line_val!=[]:
                res.append(next_line_val)
            line=next_line
            next_line=[]
            next_line_val=[]
        return res
s1=Solution()
root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)
root.right.right=Node(6)
print(s1.connect_nodes_same_level(root))