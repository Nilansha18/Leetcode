int arrangeCoins(int n) {
        int h=n, l=0;
        long long m,a;
        
        if (n==0 || n==1) return n;
        while(l<=h){
            m=(1ll*l+1ll*h)/2;
            if ((((m+1)*m)/2)> n) h=m-1;
            else if((((m+1)*m)/2)< n){
                l=m+1;
                a=m;
             }
            else return m;
        }
    return a;}
