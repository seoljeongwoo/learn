#include <iostream>
#include <cstring>
using namespace std;

int n,v[2005], dp[2005][2005];
int solve(int l, int r, int c){
    if(l > r) return 0;
    int &ret = dp[l][r];
    if(ret != -1) return ret;
    ret = max(solve(l+1,r,c+1) + v[l]*c , solve(l,r-1,c+1) + v[r]*c);
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    memset(dp,-1,sizeof(dp));
    cin >> n;
    for(int i=1; i<=n; i++) cin>>v[i];
    cout << solve(1,n,1);

}