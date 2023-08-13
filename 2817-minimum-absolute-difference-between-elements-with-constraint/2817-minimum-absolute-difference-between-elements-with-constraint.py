import bisect
class Solution:
    def minAbsoluteDifference(self, n: List[int], x: int) -> int:
        dp=[float("inf")]*len(n)
        m=float("inf")
        l=[]
        for i in range(x,len(n)):
            a=bisect.bisect_left(l,n[i-x])
            l.insert(a,n[i-x])
            a=bisect.bisect_left(l,n[i])
            if a==0:
                dp[i]=min(dp[i],abs(l[0]-n[i]))
            elif a>len(l):
                dp[i]=min(dp[i],abs(l[-1]-n[i]))
            else:
                if a>0: dp[i]=min(dp[i],abs(l[a-1]-n[i]))
                if a<len(l): dp[i]=min(dp[i],abs(l[a]-n[i]))
            m=min(m,dp[i])
        
        return m