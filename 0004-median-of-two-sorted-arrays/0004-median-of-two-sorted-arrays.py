class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len (nums1)>len(nums2):
            a=nums2
            b=nums1
        else:
            a=nums1
            b=nums2
        
        total= len(nums1)+len(nums2) 
        half=total//2
        
        l,h=0,len(a)-1
        while(True):
            m1=(l+h)//2
            m2=half-m1-2
            print(m1,m2)
            aleft= a[m1] if m1>=0 else float("-infinity")
            aright=a[m1+1] if m1+1 < len(a) else float('infinity')
            bleft= b[m2] if m2>=0 else float("-infinity")
            bright=b[m2+1] if m2+1 < len(b) else float('infinity')
           
            if( aleft<=bright and bleft<=aright):
                if (total%2==0): return (max(aleft,bleft) + min(aright,bright))/2
                else:  return min(aright,bright)
            
            elif(aleft>bright): h=m1-1
            else: l=m1+1
         
            