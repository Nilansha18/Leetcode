# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q=[]
        q.append(root)
        temp,ans=[],[]
        while q:
            n=len(q)
            for _ in range(n):
                curr=q.pop(0)
                temp.append(curr.val)
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            ans.append(temp)
            temp=[]
        return ans
              
                