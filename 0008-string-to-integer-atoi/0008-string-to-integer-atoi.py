class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="" : return 0
        if len(s)==1 :
            if  s[0].isdigit()   : return int(s[0])
            else : return 0
        i=0
        ans=""
        while i<len(s):
            if s[i]==' ':
                i+=1
            else: break
        if(i>=len(s)) : return 0
        if  s[i]=='-' or s[i]=='+': 
            ans+=s[i]
            i+=1
        if s[i]=="-" or s[i]=="+" or s[i]==" " or  65<=ord(s[i])<=126 or ord(s[i])==46 : return 0
        while(i<len(s)):
            if(s[i].isdigit() ) : 
                ans+=s[i]
                i+=1
            else : break
        
        if(len(ans)>=10): 
            if int(ans)< (-2**31 ): return (-2**31)
            if int(ans)> ((2**31)-1): return ((2**31)-1)
        return int(ans)