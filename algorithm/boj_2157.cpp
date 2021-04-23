#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int n , m, k , a , b , c, dp[305][305] , d[305][305];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m >> k;
    memset(dp,-1,sizeof(dp));
    memset(d,-1,sizeof(d));
    for(int i=0; i<k; i++){
        cin >> a >> b >> c;
        d[a][b] = max(d[a][b] , c);
    }
    
    m--;
    dp[1][0] = 0;
    for(int j=2; j<=n; j++){
        for(int i=1; i<j; i++){
            for(int k=1; k<=m; k++){
                if(d[i][j] != -1 && dp[i][k-1] !=-1){
                    dp[j][k] = max(dp[j][k] , dp[i][k-1] + d[i][j]);
                }
            }
        }
    }

    int ret =0;
    for(int i=0; i<=m;i++) ret = max(ret, dp[n][i]);
    cout << ret;
}