# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        q=[]
        level=0
        q.append(root)
        while q:
            n=len(q)
            level+=1
            for i in range(n):
                node=q.pop(0)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
        return level