class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        set<vector<int>> s;
        for(int i=0; i<nums.size();i++){
            int j=i+1;
            while(j<nums.size()){
                if((nums[j]-nums[i])==diff){
                    int k=j+1;
                    while(k<nums.size()){
                        if((nums[k]-nums[j])==diff){
                            s.insert({i,j,k});
                            
                        }
                        k++;
                    }
                }
                j++;
                
            }
        }
        return s.size();
    }
};