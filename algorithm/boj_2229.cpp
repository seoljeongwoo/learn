#include <iostream>
using namespace std;

int n, a[1005], dp[1005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for(int i=1; i<=n; i++) cin >> a[i];

    for(int i=2; i<=n; i++){
        int max_n = a[i];
        int min_n = a[i];
        for(int j=i-1; j>=1; j--){
            max_n = max(max_n , a[j]);
            min_n = min(min_n , a[j]);
            dp[i] = max(dp[i] , dp[j-1] + max_n - min_n);
        }
    }
    cout << dp[n];

}