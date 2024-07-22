class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        matrix=mat
        k=0
        while(k<4):
            for i in range(len(matrix)):
                for j in range(i):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
       
            for i in range(len(matrix)):
                matrix[i].reverse()
            if(matrix==target): return True
            else: k+=1
        return False
    