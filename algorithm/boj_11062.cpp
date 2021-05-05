#include <iostream>
#include <cstring>
using namespace std;

int a[1005], dp[1005][1005];
int solve(int l , int r, int turn){
    if( l==r) {
        return turn ? 0 : a[l];
    }
    int &ret = dp[l][r];
    if (ret != -1) return ret;
    ret = 0;
    if (turn){
        ret = min(solve(l+1,r,1-turn) , solve(l,r-1,1-turn));
    }
    else{
        ret = max(solve(l+1,r,1-turn) + a[l] , solve(l,r-1,1-turn) + a[r]);
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int tc; cin>>tc;
    for(int i=0; i<tc; i++){
        int n; cin >> n;
        for(int j=0; j<n; j++) cin >> a[j];
        memset(dp,-1,sizeof(dp));
        cout << solve(0,n-1,0) << "\n";
    }
}
