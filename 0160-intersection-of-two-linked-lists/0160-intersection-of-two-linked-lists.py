# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cnt=0
        d1=headA
        d2=headB
        while(d1 != d2):
            if(d1.next is None):
                d1=headB
                cnt+=1
            else : d1=d1.next
            
            if(d2.next is None): 
                d2=headA
                cnt+=1
            else : d2=d2.next
                
            if cnt>2 : break
        if cnt>2: return None
        return d1