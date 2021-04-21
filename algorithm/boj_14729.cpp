#include <iostream>
using namespace std;

int n ,t , a[105][2],dp[10005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> t;
    for(int i=1; i<=n; i++){
        cin >> a[i][0] >> a[i][1];
    }
    for(int i=1; i<=n; i++){
        for(int j=t; j>=a[i][0];j--) dp[j] = max(dp[j] , dp[j-a[i][0]] + a[i][1]);
    }
    cout << dp[t];
}