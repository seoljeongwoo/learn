#include <iostream>
using namespace std;

int n , a[25][25], dp[25][25][3];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    for(int i=0; i<25; i++){
        for(int j=0; j<25; j++){
            a[i][j] = 1;
        }
    }
    cin >> n;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            cin >> a[i][j];
        }
    }

    dp[1][2][0] = 1;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(a[i][j]) continue;
            if(dp[i][j][0]){
                if(a[i][j+1]==0)dp[i][j+1][0] += dp[i][j][0];
                if(a[i][j+1]==0 && a[i+1][j]==0 && a[i+1][j+1]==0)dp[i+1][j+1][2] += dp[i][j][0];
            }
            if(dp[i][j][1]){
                if(a[i+1][j]==0) dp[i+1][j][1] += dp[i][j][1];
                if(a[i][j+1]==0 && a[i+1][j]==0 && a[i+1][j+1]==0) dp[i+1][j+1][2] += dp[i][j][1];
            }
            if(dp[i][j][2]){
                if(a[i][j+1]==0) dp[i][j+1][0] += dp[i][j][2];
                if(a[i+1][j] ==0) dp[i+1][j][1] += dp[i][j][2];
                if(a[i][j+1]==0 && a[i+1][j]==0 && a[i+1][j+1] ==0) dp[i+1][j+1][2] += dp[i][j][2];
            }
        }
    }
    cout << dp[n][n][0] + dp[n][n][1] + dp[n][n][2];
}