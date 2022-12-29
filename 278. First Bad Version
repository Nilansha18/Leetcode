int firstBadVersion(int n) {
        int l=1,h=n;
        int m,a;
        
        
        while(l<=h){
            
            m=(1ll*l+1ll*h)/2 ,a; 
            if( isBadVersion(m) == true) {
                h=m-1;
                a=m;
            }
            else l=m+1;
        }
    return a;}
