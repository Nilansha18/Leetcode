# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None : return []
        
        #map with col,level as key and  , list of values as entry val
        colmap=collections.defaultdict(list)
        #queue nd initialize with first val as root for 0th col nd 0th levl
        q=collections.deque([(0,root ,0 )])
        
        #final result list
        res=[]
        
        while(q):
            #x is col no but can be used as lvel
            col , node , level = q.popleft()
            
            colmap[(col ,level)].append(node.val)
            
            if(node.left) : 
                q.append((col-1 , node.left, level+1))
            if(node.right) : 
                q.append((col+1 , node.right , level+1))
                
           
        #put elements into res , but first sorting values of same col as well as level
        for k in colmap:
            colmap[k].sort()
        res=sorted(colmap.items())
        colmap=dict(res)
        res=[]
        tempkey=float('inf')
        for k in colmap:
            if k[0]!=tempkey :
                res.append(colmap[k])
                tempkey=k[0]
            else:
                for i in range(len(colmap[k])):
                    res[-1].append(colmap[k][i])
        return res
            
            