class Solution:
    def power(self,x,n):
        if n==1:
            return x
        if n==0:
            return 1
        half=self.power(x,n//2)
        if n%2==0 : return half*half
        else : return half*half*x
        
        
            
    def myPow(self, x: float, n: int) -> float:
        if x==0 : return 0
        if n==0 : return 1
        if n<1 :
            x=1/x
            n=-n
        ans=self.power(x,n)
        return ans
   
        