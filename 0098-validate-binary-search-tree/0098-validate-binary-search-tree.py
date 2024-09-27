# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isbst(self,root,minrange,maxrange):
        if root is None : return True
    
        if root.val > minrange and root.val<maxrange :
            left=self.isbst(root.left,minrange,root.val)
            right=self.isbst(root.right,root.val,maxrange)
            return left and right
        else: return False
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini=float(-inf)
        maxi=float(inf)
        return self.isbst(root,mini,maxi)
        

        

    