class Solution {
public:
    int titleToNumber(string columnTitle) {
        int sum=0;
        for(int i=columnTitle.length()-1;i>=0;i--){
            sum+=(pow(26,columnTitle.length()-i-1) )*(int(columnTitle[i])-64);
            
        }
    return sum;}
};