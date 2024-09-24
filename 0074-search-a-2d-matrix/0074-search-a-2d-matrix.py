class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target > matrix[-1][-1] :
            return False
        l,h=0 , len(matrix)-1
        while l<=h:
            m=l + (h-l)//2
            
            if target < matrix[m][0]:
                h=m-1
            elif target > matrix[m][-1]:
                l=m+1
            elif target >= matrix[m][0] and target <=   matrix[m][-1]:
                low=0 
                high= len(matrix[m])-1
                while(low<=high):
                    mid= low + (high-low)//2
                    if matrix[m][mid] == target : return True
                    if target < matrix[m][mid] : high=mid-1
                    else: low=mid+1
                return False
        return False
        
        