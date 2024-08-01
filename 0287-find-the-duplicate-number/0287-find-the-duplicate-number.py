class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count=[0]*(len(nums))
        for i in range(len(nums)):
            count[nums[i]]=count[nums[i]]+1
            if(count[nums[i]] > 1) : return nums[i]
        return 0
            
        