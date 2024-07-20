class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]) :
                nums[i] , nums[i+1]= nums[i+1], nums[i]
                print(nums[i+1])
                j=i
                while(j>0):
                    if(nums[j]<nums[j-1]):
                        nums[j] , nums[j-1]= nums[j-1], nums[j]
                        j-=1
                    else: break
        
                        
                
        