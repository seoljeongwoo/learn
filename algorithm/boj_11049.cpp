#include <iostream>
using namespace std;

int n, a[505][2], dp[505][505];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    for(int i=1;i<=n; i++){
        cin >> a[i][0] >> a[i][1];
    }
    for(int j=2; j<=n; j++){
        for(int i=j-1; i>=1; i--){
            dp[i][j] = int(1e9);
            for(int k=i; k<j; k++){
                dp[i][j] = min(dp[i][j] , dp[i][k] + dp[k+1][j] + a[i][0]*a[k][1]*a[j][1]);
            }
        }
    }
    cout << dp[1][n];
}