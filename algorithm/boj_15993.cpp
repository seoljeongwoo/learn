#include <iostream>
using namespace std;
long long dp[100005][2];
const int mod = 1e9 + 9;
int tc , n;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    dp[1][0] = dp[2][0] = dp[2][1] = 1;
    dp[3][0] = dp[3][1] = 2;
    
    for(int i=4; i<=100000 ;i++){
        for(int j=0; j<2; j++){
            dp[i][j] += (dp[i-1][1-j] + dp[i-2][1-j] + dp[i-3][1-j])%mod;
        }
    }

    cin >> tc;
    for(int i=0; i<tc; i++){
        cin >> n;
        cout << dp[n][0] << " " << dp[n][1] << "\n";
    }

}