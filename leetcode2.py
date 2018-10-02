# Definition for singly-linked list.# class ListNode:#     def __init__(self, x):#         self.val = x#         self.next = Noneclass Solution:    def addTwoNumbers(self, l1, l2):        """        :type l1: ListNode        :type l2: ListNode        :rtype: ListNode        """        if not l1:            return l2        if not l2:            return l1        head=cur=ListNode(-1)        carry=0        while l1 and l2:            value=l1.val+l2.val+carry            if value>=10:                carry=1                value-=10            else:                carry=0            node=ListNode(value)            cur.next=node            cur=cur.next            l1=l1.next            l2=l2.next        while l1:            value=l1.val+carry            if value>=10:                carry=1                value-=10            else:                carry=0            node=ListNode(value)            cur.next=node            cur=cur.next            l1=l1.next        while l2:            value=l2.val+carry            if value>=10:                carry=1                value-=10            else:                carry=0            node=ListNode(value)            cur.next=node            cur=cur.next            l2=l2.next        if carry:            node=ListNode(1)            cur.next=node        return head.next