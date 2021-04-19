#include <iostream>
using namespace std;

const int mod = 1e9 + 9;
long long dp[1000005];
int tc, n;
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    dp[1] = 1LL; dp[2]=2LL; dp[3] = 4LL;
    for(int i=4; i<=int(1e6); i++){
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % mod;
    }
    cin >> tc;
    for(int i=0; i<tc; i++){
        cin >> n;
        cout << dp[n] << "\n";
    }

}