#include <iostream>
#include <queue>
using namespace std;

int n , m , a[101], dp[10001];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    for(int i=0; i<m; i++) cin >> a[i];
    for(int i=0; i<=n; i++) dp[i] = 1e9;
    dp[0] = 0;
    for(int i=0; i<m; i++){
        for(int j=a[i]; j<=n; j++){
            dp[j] = min(dp[j] , dp[j-a[i]] + 1);
        }
    }
    for(int i=0; i<m; i++){
        for(int j=i+1; j<m; j++){
            for(int k=a[i] + a[j] ; k<=n; k++){
                dp[k] = min(dp[k] , dp[k-a[i]-a[j]] + 1);
            }
        }
    }
    if(dp[n] == 1e9) cout << -1;
    else cout << dp[n];

}