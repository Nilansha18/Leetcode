# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Using Morris Traversal
        """
        curr=root
        while(curr is not None):
            if(curr.left is not None):
                pred=curr.left
                while(pred.right is not None):
                    pred=pred.right
                pred.right=curr.right
                curr.right=curr.left
                curr.left=None
                
            curr=curr.right
            