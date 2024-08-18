class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        x=a
        cnt=1
        rep=len(b)//len(a)
        for i in range(rep+2):
            if b in x : return cnt
            else: 
                x+=a
                cnt+=1
        return -1