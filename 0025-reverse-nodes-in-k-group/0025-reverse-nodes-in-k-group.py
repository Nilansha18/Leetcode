# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head : return None
        temp=head
        tempcount=0
        while(temp.next and tempcount<k):
            temp=temp.next
            tempcount+=1
        if tempcount< k-1 : return head
        
        curr=head
        front,prev=None,None
        cnt=0
        while(curr and cnt<k):
            front=curr.next
            curr.next=prev
            prev=curr
            curr=front
            cnt+=1
        
        if front :
            head.next= self.reverseKGroup(front , k)
            
        return prev