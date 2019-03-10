class Node:
    def __init__(self,value):
        self.left=None
        self.val=value
        self.right=None
class Solution(object):
    def drawcircle(self,r):
        n=2*r+1
        for i in range(n):
            for j in range(n):
                if (i-r)*(i-r)+(j-r)*(j-r)<=r*r:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("\n")
        return
s1=Solution()
s1.drawcircle(10)