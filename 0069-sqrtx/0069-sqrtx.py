class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        h=x
        ans=0
        while(l<=h):
            mid= l +(h-l)//2
            print(mid)
            if ( mid* mid == x):
                return mid
            elif(mid * mid > x):
                h=mid-1
            else:
                l=mid+1
                ans=mid
        return ans