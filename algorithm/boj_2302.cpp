#include <iostream>
#include <cstring>
using namespace std;
int n , m, l, r, dp[41];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    dp[0] = 1;dp[1] = 1; dp[2] = 2;
    for(int i=3; i<=n; i++) dp[i] = dp[i-1] + dp[i-2];
    int ret = 1;
    l = 1;
    for(int i=0; i<m; i++){
        cin >> r;
        ret *= dp[r-l];
        l = r+1;
    }
    ret *= dp[n-l+1];
    cout << ret;
}