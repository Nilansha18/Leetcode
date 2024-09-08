# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.preorderT(root,ans)
        return ans
    
    def preorderT(self,root , ans):
        if(root is None):
            return
        ans.append(root.val)
        self.preorderT(root.left , ans)
        self.preorderT(root.right , ans)
    