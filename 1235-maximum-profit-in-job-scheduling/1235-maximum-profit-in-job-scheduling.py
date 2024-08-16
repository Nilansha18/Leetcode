class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n=len(profit)
        jobs=[ [  startTime[i],endTime[i],profit[i] ]  for i in range(n) ]
        jobs=sorted(jobs , key=lambda x : x[0] )
        print (jobs)
        
        memo={}

        def solve(jobs,n,i):
            if(i>=n): return 0
            if i in memo : return memo[i]

            next = getNextIndex(jobs,i+1,jobs[i][1])
            taken= jobs[i][2] + solve(jobs, n , next)
     
            notTaken = solve(jobs,n,i+1)

            memo[i]=max(taken, notTaken)

            return memo[i]

        def getNextIndex( jobs, l ,currjobEndtime):
            r=len(jobs)-1
            result=r+1
            while(l<=r):
                mid= l + (r-l)//2
                if(jobs[mid][0] >= currjobEndtime):
                    result=mid
                    r=mid-1
                else: l=mid+1
            return result


        return  solve(jobs,n,0)