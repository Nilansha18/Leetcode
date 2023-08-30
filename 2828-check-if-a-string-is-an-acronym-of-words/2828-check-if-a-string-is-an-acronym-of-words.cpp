class Solution {
public:
    bool isAcronym(vector<string>& words, string s) {
        if(words.size()!=s.length()) return false;
        else{
            for(int i=0; i<words.size();i++){
                string x=words[i];
                cout<<x<<" ";
                if(x[0]!=s[i]) return false;
                else continue;
            }
            return true;
        }
    return false;}
};