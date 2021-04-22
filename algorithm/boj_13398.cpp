#include <iostream>
#include <cstring>
using namespace std;

int n, a[100005], dp[100005][2];

int main(){
    ios_base ::sync_with_stdio(false);
    cin.tie(0);

    memset(dp,-1,sizeof(dp));
    cin >> n;
    for(int i=1; i<=n ;i++) cin >> a[i];
    int ret = a[1];
    dp[1][0] = a[1];
    for(int i=2; i<=n; i++){
        dp[i][0] = max(dp[i-1][0] + a[i] , a[i]);
        dp[i][1] = max(dp[i-1][1] + a[i] , dp[i-1][0]);
        ret = max(ret, max(dp[i][0] , dp[i][1]));
    }
    cout << ret;
}