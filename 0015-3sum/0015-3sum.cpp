class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(),nums.end());
        set <vector<int>> s;
        for(int i=0;i<nums.size();i++){
            int j=i+1;
            int k=nums.size()-1;
            while(j<k){
                if((nums[k]+nums[j]+nums[i])==0){
                    s.insert({nums[i],nums[j],nums[k]});
                    j++;
                    k--;
                }
                else if ((nums[k]+nums[j]+nums[i]) < 0) j++;
                else k--;
            }
            
        }
        for(auto i:s){
            ans.push_back(i);
        }
        return ans;
    }
};