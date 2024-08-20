class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[len(nums) - 1] != nums[len(nums) - 2]:
            return nums[len(nums) - 1]
        
        
        res1=nums[0]
        res2=nums[-1]
        for i in range(1,(len(nums)//2)+1):
            res1 = res1 ^ nums[i]
            res2 = res2 ^ nums[-(i+1)]
            print(res1 , res2)
            if (res1!=0 and res1!= nums[i]): return nums[i-1]
            if (res2!=0 and res2!= nums[-(i+1)]): return nums[-i]
        if(res1!=res2):res=res1^res2
        else : res=res1
        return res
            