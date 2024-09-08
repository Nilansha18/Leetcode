# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        pred= TreeNode()
        curr= root
        while(curr is not None):
            if(curr.left is None):
                ans.append(curr.val)
                curr=curr.right
            else:
                pred=curr.left
                while( pred.right is not None and pred.right!=curr):
                    pred=pred.right
                
                #link creation
                if(pred.right is None):
                    pred.right=curr
                    curr=curr.left
                    
                #link deletion
                else:
                    pred.right=None
                    ans.append(curr.val)
                    curr=curr.right
        return ans
  
            
        