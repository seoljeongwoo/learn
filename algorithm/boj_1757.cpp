#include <iostream>
#include <cstring>
using namespace std;

int n, m, d[10005],dp[10005][505];
int solve(int c, int p){
    if( c == n+1) {
        if ( p ==0) return 0;
        else return -int(1e9);
    }
    int &ret = dp[c][p];
    if(ret != -1) return ret;
    ret = -int(1e9);
    if(p<m)ret = max(ret, solve(c+1,p+1) + d[c]);
    if(p >0){
        if(c+p <= n+1) ret = max(ret, solve(c+p,0));
    }
    else if(p==0){
        ret = max(ret, solve(c+1,0));
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    memset(dp,-1,sizeof(dp));
    cin >> n>> m;
    for(int i=1; i<=n; i++) cin >> d[i];
    cout << solve(1,0);


}