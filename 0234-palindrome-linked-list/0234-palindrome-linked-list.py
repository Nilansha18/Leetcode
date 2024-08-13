# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cnt=1
        temp=head
        list1=[]
        list2=[]
        while(temp.next is not None):
            temp=temp.next
            cnt+=1
        for i in range(cnt//2):
            list1.insert(0,head.val)
            head=head.next
        if(cnt%2!=0): 
            list1.insert(0,head.val)
            list2.append(head.val)
            if list1[0]!=list2[0]: return False
            head=head.next
            
            for i in range(cnt//2 ):
                list2.append(head.val)
                head=head.next  
                if list1[i+1]!=list2[i+1]: return False
            
        else : 
            for i in range(cnt//2 ):
                list2.append(head.val)
                head=head.next  
                if list1[i]!=list2[i]: return False
        return True
        
        
            