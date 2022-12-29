int mySqrt(int x) {
        long long low=1, high=x;
        long long mid, ans=0;
        if (x==0 || x==1) return x;
        while (low<=high){
            mid=(low+high)/2;
            if(mid*mid==x) 
            return (int)mid;
            else if (mid*mid>x)
             high=mid-1;
            else{
                low=mid+1;
                ans=mid;   
            }
        }
    return (int)ans;
    }
