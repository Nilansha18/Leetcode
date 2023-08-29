class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
        int cnt1=0, cnt2=0;
        for(int i=0;i<moves.length();i++){
            if(moves[i]=='R' || moves[i]=='_') cnt1++;
            if(moves[i]=='L') cnt1--;
        }
        for(int i=0;i<moves.length();i++){
            if(moves[i]=='L' || moves[i]=='_') cnt2++;
            if(moves[i]=='R') cnt2--;;
        }
        if(cnt1>=abs(cnt2)) return cnt1;
        else return abs(cnt2);
    }
};