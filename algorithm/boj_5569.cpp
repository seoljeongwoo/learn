#include <iostream>
#include <cstring>
using namespace std;

int w,h,dp[105][105][2];
const int mod = 1e5;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> w >> h;
    dp[1][1][0] = dp[1][1][1] = 1;
    for(int i=1; i<=h; i++){
        for(int j=1; j<=w; j++){
            if(dp[i][j][0]){
                dp[i][j+1][0] += dp[i][j][0];
                dp[i+1][j+1][1] += dp[i][j][0];
                dp[i][j+1][0] %= mod;
                dp[i+1][j+1][1] %= mod;
            }
            if(dp[i][j][1]){
                dp[i+1][j][1] += dp[i][j][1];
                dp[i+1][j+1][0] += dp[i][j][1];
                dp[i+1][j][1] %= mod;
                dp[i+1][j+1][0] %= mod;
            }
        }
    }
    cout << (dp[h][w][0] + dp[h][w][1]) % mod  <<"\n";

}