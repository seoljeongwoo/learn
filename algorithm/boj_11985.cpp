#include <iostream>
#include <algorithm>
using namespace std;

int n , m;
long long k , dp[20005] , a[20005];
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m >> k;
    for(int i=1; i<=n; i++) {
        cin >> a[i];
    }
    for(int i=1; i<=n ;i++){
        dp[i] = 1e15;
        long long max_n = a[i];
        long long min_n = a[i];
        for(int j=i; j>= max(1LL , (long long)i-m+1); j--){
            max_n = max (max_n , a[j]);
            min_n = min (min_n , a[j]);
            dp[i] = min(dp[i], dp[j-1] + k + (i-j+1)*(max_n - min_n));
        }
    }
    cout << dp[n];
}