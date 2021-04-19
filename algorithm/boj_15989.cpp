#include <iostream>
using namespace std;

int dp[10001][3] , tc , n;
int main(){
    ios_base:: sync_with_stdio(false);
    cin.tie(0);

    dp[1][0] = 1;
    dp[2][0] = 1;
    dp[2][1] = 1;
    dp[3][0] = 2;
    dp[3][2] = 1;
    for(int i=4; i<=10000; i++){
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2];
        dp[i][1] = dp[i-2][1] + dp[i-2][2];
        dp[i][2] = dp[i-3][2];
    }
    cin >> tc;
    for(int i=0; i<tc; i++){
        cin >> n;
        cout << dp[n][0] + dp[n][1] + dp[n][2] << "\n";
    }
}