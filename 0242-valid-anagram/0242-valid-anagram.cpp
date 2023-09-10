class Solution {
public:
    bool isAnagram(string s, string t) {
        int cnt=0;
        if(s.length()!=t.length()) return false;
        for(int i=0; i<s.length(); i++){
            int j=0;
            while(j<t.length()){
                if(s[i]==t[j]){
                  t.erase(t.begin() + j);
                  cnt++;  
                  j=t.length();
                } 
                else j++;
            }
        }
        if(cnt==s.length()) return true;
        else return false;
    }
};