from collections import defaultdict
class Solution:
    def maxSum(self, n: List[int]) -> int:
        m=defaultdict(list)
        for i in n:
            n=max(str(i))
            m[n].append(i)
        ma=-1
        for i in m:
            if len(m[i])>1:
                for j in range(0,len(m[i])):
                    for k in range(0,j):
                        ma=max(ma,m[i][j]+m[i][k])
        return ma