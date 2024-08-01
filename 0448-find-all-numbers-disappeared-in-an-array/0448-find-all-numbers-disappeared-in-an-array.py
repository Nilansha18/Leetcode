class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count=[0]*(len(nums)+1)
        for i in range(len(nums)):
            count[nums[i]] = count[nums[i]] +1
        j=1
        ans=[]
        while(j<len(count)):
            if(count[j]==0): ans.append(j)
            j+=1
        return ans