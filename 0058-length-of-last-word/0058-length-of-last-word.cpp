class Solution {
public:
    int lengthOfLastWord(string s) {
        int cnt=0;
        for(int i=s.length()-1; i>=0; i--){
            if(cnt==0 && int(s[i])==32) continue;
            if(cnt!=0 && int(s[i])==32) return cnt;
            if(int(s[i])!=32) {
                cnt++;
                continue;
            }
        }
        return cnt;
    }
};