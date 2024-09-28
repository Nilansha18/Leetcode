class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                k=i
                cnt=0
                for j in range(len(needle)):
                    if haystack[k]==needle[j]:
                        cnt+=1
                        k+=1
                    else : break
                if cnt==len(needle): return i
        return -1
                
        