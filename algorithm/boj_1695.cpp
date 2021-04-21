#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int n,a[5005],dp[2][5005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    for(int i=1; i<=n; i++) cin >> a[i];
    int t = 0;
    for(int i=n; i>=1; i--){
        for(int j=1; j<=n; j++){
            if(a[i] == a[j]) dp[t][j] = dp[1-t][j-1] +1;
            else dp[t][j] = max(dp[1-t][j], dp[t][j-1]);
        }
        t = 1-t;
    }
    cout << n - dp[1-t][n];
}