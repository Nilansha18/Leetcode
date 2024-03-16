class Solution {
public:
    string finalString(string s) {
        for(int i=0;i<s.length();i++){
            if(s[i]=='i'){
                int j=i-1;
                while(j>i-1-j){
                    char a=s[j];
                    s[j]=s[i-1-j];
                    s[i-1-j]=a;
                    j--;
                }
                s.erase(i,1);
                i--;
            }
        }
        return s;
    }
};