# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if(head.next is None or (left==right)): return head
        if(left>1) : orghead=head
        head2=ListNode()
        for _ in range(left-1):
            head2=head
            head=head.next
        
        tempnode=head 
        prev=None
        curr=head
        for _ in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            
        head2.next=prev
        tempnode.next=curr
        
        if(left==1) : return prev
        else : return orghead
            
        
        