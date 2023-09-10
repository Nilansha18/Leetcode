class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        for(int i=1;i<words.size();i++){
            if(words[i-1].length()==words[i].length() ) {
                string x=words[i-1];
                string y=words[i];
                sort(x.begin(), x.end());
                sort(y.begin(), y.end()); 
                if(x==y) {
                    words.erase(words.begin()+i);
                    i--;
                }
            }
            else continue;
        }
        return words;
    }
};