class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int cnt=0;
        if(flowerbed.size()==1){  
            if(flowerbed[0]==0) cnt+=1;
            if(cnt>=n) return true;
            else return false;
        }
        if(flowerbed[0]==0 && flowerbed[1]==0){
            flowerbed[0]=1;
            cnt+=1;
        }
        if(cnt>=n) return true;
        cout<<cnt<<" ";
        for(int i=1;i<flowerbed.size()-1;i++){
            if(flowerbed[i-1]==0 && flowerbed[i]==0 && flowerbed[i+1]==0) {
                flowerbed[i]=1;
                cnt+=1;
                
                
            }
            if(cnt>=n) return true;
            
        }
        int x=flowerbed.size()-1;
        if(flowerbed[x]==0 && flowerbed[x-1]==0){
            cnt+=1;
        }
        if(cnt>=n) return true;
        return false;
    }
};