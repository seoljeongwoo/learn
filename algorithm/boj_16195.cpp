#include <iostream>
using namespace std;

long long dp[1005][1005];
const int mod = 1e9 + 9;
int tc, n , m;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    dp[1][1]=dp[2][2]=dp[2][1]=dp[3][3]=dp[3][1]= 1;
    dp[3][2] = 2;
    for(int i=4; i<=1000; i++){
        for(int j=1; j<=3; j++){
            for(int k=1; k<=i; k++){
                if(dp[i-j][k-1] ==0) continue;
                dp[i][k] += dp[i-j][k-1];
                dp[i][k] %= mod;
            }
        }
    }
    cin >> tc;
    for(int i=0; i<tc; i++){
        cin >> n>> m;
        long long ret = 0;
        for(int k=1; k<=m; k++){
            ret += dp[n][k];
            ret %= mod;
        }
        cout << ret << "\n";
    }
}