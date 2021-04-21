#include <iostream>
#include <cstring>
using namespace std;

int t,n,c[25],dp[10005],m;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> t;
    for(int i=0; i<t; i++){
        memset(dp,0,sizeof(dp));
        cin >> n;
        dp[0] = 1;
        for(int j=0; j<n ; j++) cin >> c[j];
        cin >> m;
        for(int j=0; j<n; j++){
            for(int k= c[j]; k<=m; k++) dp[k] += dp[k-c[j]];
        }
        cout << dp[m] << "\n";
    }
}