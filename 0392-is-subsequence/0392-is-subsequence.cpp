class Solution {
public:
    bool isSubsequence(string s, string t) {
        int j=0, c=s.size();
        for(int i=0; i<s.size();i++){
            while(j<t.size()){
                if(s[i]==t[j]) {
                    c--;
                    j++;
                    break;
                }
                j++;
            }
        }
        if (c==0) return true;
        return false;
    }
};