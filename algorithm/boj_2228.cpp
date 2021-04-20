#include <iostream>
#include <cstring>
using namespace std;

int n , m , dp[105][55] , a[105];
int solve(int c, int p){

    if( p ==0) return 0;
    if( c >= n) return -int(1e9);
    int &ret = dp[c][p];
    if(ret != -1) return ret;
    ret = solve(c+1,p);
    int s =0 ;
    for(int i=c; i<n ; i++){
        s += a[i];
        ret = max(ret, solve(i+2,p-1) + s);
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;
    memset(dp,-1,sizeof(dp));
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    cout << solve(0,m);
}