#include <iostream>
#include <cstring>
using namespace std;

int n,a[50005], dp[50005][3],m;
int solve(int curr, int trail){
    if(trail == 3 || curr > n) return 0;
    int &ret = dp[curr][trail];
    if(ret != -1) return ret;
    ret = solve(curr+1, trail); // Not
    ret = max(ret, solve(curr+m,trail+1)+a[min(n,curr+m-1)] - a[curr-1]);
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    for(int i=1; i<=n; i++) cin >> a[i] , a[i] += a[i-1];
    cin >> m;
    memset(dp,-1,sizeof(dp));
    cout << solve(1,0);

}