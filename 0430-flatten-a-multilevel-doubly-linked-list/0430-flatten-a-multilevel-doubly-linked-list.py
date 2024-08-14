"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if (head is None or ( head.next is None and head.child is None ) ) : return head
        
        temp=head
        stack = deque()
        while(temp.next is not None or temp.child is not  None ):
            if(temp.child is not None):
                stack.append(temp.next)
                temp.next=temp.child
                temp.child.prev=temp
                temp.child=None
            temp=temp.next
            if(temp.next is None and stack and stack[-1] is not None):
                temp2 = Node()
                temp2=stack.pop()
                temp.next=temp2
                temp2.prev=temp
            
                
               
        return head