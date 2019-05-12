class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		ListNode dummy(0);
		ListNode* last=&dummy;
		int carry=0;
		while(l1!=0 || l2 !=0 ||carry!=0){
			int val=carry;
			if(l1!=0){val+=l1->val;l1=l1->next;}
			if(l2!=0){val+=l2->val;l2=l2->next;}
			carry=val/10;
			val%=10;
			last->next=new ListNode(val);
			last=last->next;
		}
		return dummy.next;
    }
};