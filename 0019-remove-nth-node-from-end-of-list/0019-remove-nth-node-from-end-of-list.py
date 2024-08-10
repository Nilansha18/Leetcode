# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt=0
        temp=head
        temp2=head
        while ( temp is not None):
            cnt+=1
            temp=temp.next
        for i in range(abs(cnt-n-1)):
            temp2=temp2.next
        if cnt==n : 
            head=head.next
            return head
        
        temp2.next=temp2.next.next
        return head
            