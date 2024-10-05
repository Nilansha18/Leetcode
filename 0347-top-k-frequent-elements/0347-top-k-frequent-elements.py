from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        mymap=defaultdict(int)
        for i in range(len(nums)):
            mymap[nums[i]]+=1
        
        count=[[] for i in range(len(nums)+1) ]
        for key,value in mymap.items():
            count[value].append(key)
        for i in range(len(count)-1,0,-1):
            if len(count[i]) !=0 :
                for n in count[i]:
                    ans.append(n)
                    if len(ans)==k : return ans
            
        return ans