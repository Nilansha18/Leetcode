class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        string x;
        int  n=words.size();
        for(int i=0;i<n;i++){
            int j=0;
            x.clear();
            while(j<words[i].length()){
                if(words[i][j]!=separator) x+=words[i][j];
                if(words[i][j]==separator) {
                    if(x.length()!=0) words.push_back(x);
                    x.clear();
                }
                j++;
                
            }
            if(x.length()!=0) words.push_back(x);
        }
        words.erase(words.begin(), words.begin() + n);
        for(int i=0;i<n;i++){
            cout<<words[i]<<" ";
        }
        return words;
    }
};