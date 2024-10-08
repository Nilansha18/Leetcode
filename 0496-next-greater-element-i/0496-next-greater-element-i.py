class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1idx= { n : i for i,n in enumerate(nums1)}
        result=[-1]*len(nums1)
        
        stack=[]
        for i in range(len(nums2)):
            cur= nums2[i]
            while stack and cur>stack[-1]:
                val=stack.pop()
                idx=nums1idx[val]
                result[idx]=cur
            if ( cur in nums1):
                stack.append(cur)
        return result