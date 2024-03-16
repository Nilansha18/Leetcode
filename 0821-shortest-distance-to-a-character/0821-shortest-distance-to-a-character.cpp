class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int> answer, x;
        for(int i=0; i<s.length();i++){
            if(s[i]==c) x.push_back(i);
        }
        int j=0;
        while(j<s.length()){
            int y=abs(j-x[0]);
            for(int i=1; i<x.size();i++){
                if(abs(j-x[i]) < y) y=abs(j-x[i]);
            }
            answer.push_back(y);
            j++;
        }
        return answer;
        
    }
};