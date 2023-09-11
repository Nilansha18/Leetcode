class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int ans=0,cnt=0;
        for(int i=0; i<prices.size();i++){
            int j=i+1;
            while(j<prices.size()){
                int sum=(prices[i]+prices[j]);
                if(sum<=money){ 
                    cnt++;
                    if((money-sum)>ans) ans=(money-sum);
                }
                j++;
            }
        }
        if(cnt==0) return money;
        return ans;
    }
};