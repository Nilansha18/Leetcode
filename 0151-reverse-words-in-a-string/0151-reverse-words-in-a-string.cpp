class Solution {
public:
    string reverseWords(string s) {
        int x=s.length(),y=0;
        
        for(int i=x-1 ; i>=0;i--){
            if( i==0 || (s[i]==' ' && s[i+1]!=' ')){
                y=i+1;
                if(i==0 && s[i]!=' ') y=0;
                cout<<y<<' ';
                while(y<x && s[y]!=' '){
                    s.push_back(s[y]);
                    y++;
                }
                if(i!=0 && i< x-1)s.push_back(' ');
               
            
	

                
            }
        }
        s.erase(0,x);
        if(s[s.length()-1]==' ') s.erase(s.length()-1,1);
        return s;

	
    }
};