# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None : return []
        ans=[]
        q=[]
        lr = True
        index=0
        q.append(root)
        while( len(q)!=0):
            temp=[]
            x=len(q)
            for i in range(x):
                curr=q.pop(0)
                if lr:
                    temp.append(curr.val)
                else:
                    temp.insert(0, curr.val)
                if(curr.left is not None): q.append(curr.left)
                if(curr.right is not None): q.append(curr.right)
            lr=not lr
            ans.append(temp)
              
        return ans
            
            