#include <iostream>
using namespace std;

int n , k, a[1005][2],dp[10005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> k;
    for(int i=1; i<=k; i++){
        cin >> a[i][0] >> a[i][1];
    }
    for(int i=1; i<=k; i++){
        for(int j=n; j>=a[i][1]; j--) dp[j] = max(dp[j] , dp[j-a[i][1]] + a[i][0]);
    }
    cout << dp[n];

}