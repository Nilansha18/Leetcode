class Solution {
public:
    int appendCharacters(string s, string t) {
        int cnt=0,y=0;
        for(int i=0;i<t.length();i++){
            
            while(y<s.length()){
                if(t[i]==s[y]){
                    cnt++;
                    y++;
                    break;
                }
                y++;
            }
            
        }
        return t.length()-cnt;
    }
};