class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=[]
        col=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j]==0): 
                    row.append(i)
                    col.append(j)
        
        for r in row: 
            y=len(matrix[0])-1
            while(y>=0):
                matrix[r][y]=0
                y-=1
        for c in col:
            x=len(matrix)-1
            while(x>=0):
                matrix[x][c]=0
                x-=1
            
        