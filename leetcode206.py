# Definition for singly-linked list.class ListNode(object):     def __init__(self, x):         self.val = x         self.next = Noneclass Solution(object):    def reverseList(self, head):        """        :type head: ListNode        :rtype: ListNode        """        pre,cur,next1=None,head,head        while next1:            cur=next1            next1=next1.next            cur.next=pre            pre=cur        return pres=Solution()head=ListNode(1)head.next=ListNode(2)head.next.next=ListNode(3)print(s.reverseList(head))