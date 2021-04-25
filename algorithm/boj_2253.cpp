#include <iostream>
#include <cstring>
using namespace std;

int n,m,dp[10005][150],unused[10005] , a;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;
    for(int i=0; i<m; i++) {
        cin >> a;
        unused[a] = 1;
    }
    memset(dp,-1,sizeof(dp));
    dp[2][1] = 1;
    for(int i=2; i<=n; i++){
        if(unused[i]) continue;
        for(int k=1; k<=150;k++){
            if(dp[i][k] != -1){
                if(i+k-1 <= n) dp[i+k-1][k-1] == -1 ? dp[i+k-1][k-1] = dp[i][k]+1 : dp[i+k-1][k-1]= min(dp[i+k-1][k-1] , dp[i][k]+1);
                if(i+k <=n) dp[i+k][k] == -1 ? dp[i+k][k] = dp[i][k] + 1 : dp[i+k][k] = min(dp[i+k][k] , dp[i][k] + 1);
                if(i+k+1<=n) dp[i+k+1][k+1] == -1 ? dp[i+k+1][k+1] = dp[i][k] + 1 : dp[i+k+1][k+1] = min(dp[i+k+1][k+1] , dp[i][k] + 1);
            }
        }
    }
    int ret = int(1e9);
    for(int i=1; i<=150; i++) {
        if(dp[n][i] == -1) continue;
        ret = min(ret, dp[n][i]);
    }
    if(ret == int(1e9)) ret = -1;
    cout << ret;
}