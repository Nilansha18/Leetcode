class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapp={}
        for index,val in enumerate(nums):
            diff=target-val
            if  diff in mapp:
                return [index,mapp[diff]]
            mapp[val]=index       
        
        return [0,0]