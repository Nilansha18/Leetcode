# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.postorderT(root,ans)
        return ans
    
    def postorderT(self,root , ans):
        if(root is None):
            return
        
        self.postorderT(root.left , ans)
        self.postorderT(root.right , ans)
        ans.append(root.val)