# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head.next is None): return True
        if(head.next.next is None): 
            if(head.val==head.next.val): return True
            else : return False
        if(head.next.next.next is None):
            if(head.val==head.next.next.val): return True
            else : return False
        slow=head
        fast=head
        temp=ListNode()
        
        while(fast.next is not None and fast.next.next is not None):
            slow=slow.next
            fast=fast.next.next
            
        print(fast)
        
        #oddcase
        if(fast.next is None):
            temp.val=slow.val
            temp.next=slow.next
            slow.next=None
            
        else:
            temp=slow.next
            slow.next=None
            
        
        prev=None
        while(head is not None ):
            temp2=head.next
            head.next=prev
            prev=head
            head=temp2
        
        while(temp is not None or prev is not None):
            if(temp.val!=prev.val): return False
            else: 
                temp=temp.next
                prev=prev.next
        
        return True
        
        
            