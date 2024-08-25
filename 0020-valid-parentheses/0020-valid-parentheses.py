class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if (s[i]== '(' or s[i]=='{' or s[i]=='[') :
                stack.append(s[i])
                
            elif (len(stack)==0): 
                if(  s[i]==')' or  s[i]=='}' or  s[i]==']') : return False
                
            else :
                if ( (stack[-1]== '(' and s[i]==')' )or (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']')): stack.pop()
                
                else : 
                    return False
        if len(stack)==0 : return True
        return False