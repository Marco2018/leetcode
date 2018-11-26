class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
class Solution(object):
    def detectloop(self,head):
        slow=fast=head.next
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
s1=Solution()
head=Node(-1)
head.next=Node(1)
head.next.next=Node(2)
head.next.next.next=Node(3)
head.next.next.next.next=Node(4)
head.next.next.next.next.next=Node(5)
head.next.next.next.next.next.next=head.next.next
print(s1.detectloop(head))