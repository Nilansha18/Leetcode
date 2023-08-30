class Solution {
public:
    int strStr(string haystack, string needle) {
        int ans=-1;
        for(int j=0; j<haystack.length();j++) {
            if(needle[0]==haystack[j]) {
                ans=j;
                for(int i=1;i<needle.length();i++){
                    if(needle[i]!=haystack[j+i]) {
                        cout<<ans<<" ";
                        ans=-1;
                        break;
                    }
                    else continue;
                    
                }
                if(ans!=-1) return ans;
            }
            
        }
    return ans;}
    
};