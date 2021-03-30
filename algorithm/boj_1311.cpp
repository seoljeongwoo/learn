#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int n, dp[(1<<21)], m[21][21];
int solve(int idx,int bit){
    if (bit == (1<<n)-1) return 0;
    int &ret = dp[bit];
    if(ret != -1) return ret;
    ret = int(1e9);
    for(int i=0; i<n; i++){
        if(!(bit&(1<<i))) ret = min(ret, solve(idx+1,bit|(1<<i))+m[idx][i] );
    }
    return ret;
}
int main(){
    ios_base :: sync_with_stdio(false);
    cin >> n;
    memset(dp,-1, sizeof(dp));
    for(int i=0; i<n; i++) for(int j=0; j<n; j++) cin >> m[i][j];
    int ans = int(1e9);
    for(int i=0; i<n; i++){
        ans = min(ans, m[0][i] + solve(1, (1<<i)));
    }
    cout << ans;
}