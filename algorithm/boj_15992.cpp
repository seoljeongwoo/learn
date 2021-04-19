#include <iostream>
using namespace std;

long long dp[1005][1005];
const int mod = 1e9 + 9;
int tc ,n,m;
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    dp[1][1] = 1;
    dp[2][1] = 1;
    dp[2][2] = 1;
    dp[3][1] = 1;
    dp[3][2] = 2;
    dp[3][3] = 1;
    for(int i=4; i<=1000; i++){
        for(int k=1; k<=3; k++){
            for(int j=1; j<=i; j++){
                if(dp[i-k][j-1] ==0 ) continue;
                dp[i][j] += dp[i-k][j-1];
                dp[i][j] %= mod;
            }
        }
    }

    cin >> tc;
    for(int i=0; i<tc; i++){
        cin >> n >> m;
        cout << dp[n][m]%mod << "\n";
    }
}