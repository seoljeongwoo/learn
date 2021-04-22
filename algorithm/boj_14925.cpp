#include <iostream>
using namespace std;

int m, n , a[1005][1005], dp[1005][1005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> m >> n;
    for(int i=0;i <m; i++){
        for(int j=0; j<n; j++){
            cin >> a[i][j];
        }
    }
    int ret =0 ;
    for(int i=0; i<m; i++) {
        if(a[i][0] == 0) dp[i][0] = 1;
        else dp[i][0] = 0;
        ret = max(ret, dp[i][0]);
    }
    for(int j=0; j<n; j++){
        if(a[0][j] ==0) dp[0][j] = 1;
        else dp[0][j] = 0;
        ret = max(ret , dp[0][j]);
    }
    for(int i=1; i<m; i++){
        for(int j=1; j<n; j++){
            if(a[i][j] !=0) {
                dp[i][j] = 0; 
            }
            else if(a[i-1][j-1] ==0 && a[i][j-1] ==0 && a[i-1][j] == 0){
                dp[i][j] = min(dp[i-1][j-1] , min(dp[i][j-1] , dp[i-1][j])) + 1;
            }
            else dp[i][j] = 1;
            ret = max(ret, dp[i][j]);
        }
    }
    cout << ret;

}