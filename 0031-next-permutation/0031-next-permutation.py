class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        ind=-1
        for i in range(-2,-len(nums)-1 , -1):
            if (nums[i]<nums[i+1]) :
                ind=i
                break
                
        if(ind==-1): return nums.reverse()
        else:
            for i in range(-1,ind,-1):
                if(nums[i]>nums[ind]):
                    nums[i] , nums[ind] = nums[ind] , nums[i]
                    print(nums)
                    break
            print(ind)
            nums[ind+len(nums)+1 : len(nums)]=reversed(nums[ind+len(nums)+1  : len(nums)])
            
        return nums