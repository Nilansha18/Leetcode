# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sta=[]
        h=None
        a=None
        b=head
        while b!=None:
            a=b.next
            b.next=h
            h=b
            b=a
        c=0
        a=h
        while a!=None:
            b=a
            d=a.val
            d=d*2+c
            a.val=d%10
            c=d//10
            a=a.next
        if c==1:
            b.next=ListNode(c,None)
        a=h
        b=h
        h=None
        while b!=None:
            a=b.next
            b.next=h
            h=b
            b=a
        
        return h
        