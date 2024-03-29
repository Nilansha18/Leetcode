class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if(nums.size()==1) return nums[0];
        sort(nums.begin(), nums.end());
        int cnt=1; 
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]==nums[i+1]) {
                cnt++;
            }
            else{
                if(cnt>(nums.size()/2)) return nums[i];
            }
        }
        if(cnt>(nums.size()/2)) return nums[nums.size()-1];
   return 0; }
};