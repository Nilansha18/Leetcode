class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ans;
        int diff=word1.length() - word2.length();
        if(diff>=0){
            for(int i=0; i<word2.length();i++){
                ans+=word1[i];
                ans+=word2[i];
            }
            int y=word2.length();
            while(diff>0 && y<word1.length()){
                ans+=word1[y];
                y++;
            }
            
        }
        else{
            for(int i=0; i<word1.length();i++){
                ans+=word1[i];
                ans+=word2[i];
            }
            int x=word1.length();
            while(x<word2.length()){
                ans+=word2[x];
                x++;
            }
            
        }
        return ans;
    }
};