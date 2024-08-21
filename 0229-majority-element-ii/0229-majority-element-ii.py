class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count =defaultdict(int)
        for n in nums:
            count[n]+=1
            if(len(count)<=2): continue
            else:
                new_cnt=defaultdict(int)
                for n,c in count.items():
                    if c>1 : new_cnt[n]=c-1
                count=new_cnt
        res=[]
        for n in count:
            if  nums.count(n) > len(nums)//3 : res.append(n)
        return res      