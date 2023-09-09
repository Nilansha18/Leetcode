class Solution {
public:
    string addBinary(string a, string b) {
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        int k=0;
        if(a.length()<b.length()){
            int diff=b.length()-a.length();
            while(k<diff){
                a+="0";
                k++;
            }
        } 
        if(a.length()>b.length()) {
            int diff=a.length()-b.length();
            while(k<diff){
                b+="0";
                k++;
            }
        }
        
        vector<int> ans;
        int carry=0;
        int sum=0;
        for(int i=0; i<a.length();i++){
            cout<<a[i]<<" "<<b[i]<<endl;
            sum=(int(a[i])-48)+(int(b[i])-48)+carry;
            if(sum==0){
                ans.push_back(0);
                carry=0;
            }
            if(sum==1){
                ans.push_back(1);
                carry=0;
            }
            if(sum==2){
                ans.push_back(0);
                carry=1;
            }
            if(sum==3){
                ans.push_back(1);
                carry=1;
            }
        }
        
        if(carry!=0) ans.push_back(carry);
        
        string z;
        for(int i=ans.size()-1;i>=0;i--){
            z=z+ (to_string(ans[i]));

        }
        return z;

    }
};