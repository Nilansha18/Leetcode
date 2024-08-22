class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        print(nums)
        median=0
        l,h=0,len(nums)-1
        mid=(l+h)//2
        #even
        if (len(nums)%2==0): 
            mid2=(l+h)//2 + 1
            median = (nums[mid]+nums[mid2])/2
        #odd
        else:
            median = nums[mid]
        return median
            