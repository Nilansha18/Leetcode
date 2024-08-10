# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 is None and list2 is None): return list1
        if (list1 is None and list2 is not None): return list2
        if (list1 is not None and list2 is  None): return list1
        pt1=list1
        pt2=list2
        newhead=ListNode()
        temp=ListNode()
        while(pt1 is not None and pt2 is not None):
            
            if((pt1.val)<=(pt2.val)):
                
                if(newhead.val is 0): 
                    
                    newhead=pt1
                    print (newhead)
                    temp=pt1
                else: 
                    temp.next=pt1
                    temp=temp.next
                pt1=pt1.next
            else:
                if(newhead.val is 0): 
                    newhead=pt2
                    temp=pt2
                else : 
                    temp.next=pt2
                    temp=temp.next
                pt2=pt2.next
        if(pt1 is None): temp.next=pt2
        if(pt2 is None): temp.next=pt1
            
        return newhead