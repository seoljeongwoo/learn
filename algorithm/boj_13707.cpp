#include <iostream>
using namespace std;

const int mod = 1e9;
int n , k;
long long dp[5005][5005];
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> k;
    for(int i=0; i<=n ;i++) {
        dp[i][1] = 1;
        if(i) dp[i][1] += dp[i-1][1];
        dp[i][1] %= mod;
    }
    for(int j=2; j<=k; j++){
        for(int i=0; i<=n; i++) {
            dp[i][j] = dp[i][j-1];
            if(i && j!=k) dp[i][j] += dp[i-1][j];
            dp[i][j] %= mod;
        }
    }
    cout << dp[n][k] % mod;

}