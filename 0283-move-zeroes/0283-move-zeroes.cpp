class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int x=nums.size();
        for (int i=0;i<nums.size();i++){
            if(nums[i]==0 && x>0) {
                cout<<i;
                nums.erase(nums.begin()+i);
                nums.push_back(0);
                i-=1;
                x-=1;
            }

            
        }
        
    }
};