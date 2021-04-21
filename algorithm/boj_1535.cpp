#include <iostream>
#include <algorithm>
using namespace std;

int n,a[25],b[25],dp[105];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for(int i=1; i<=n; i++) cin >> a[i];
    for(int i=1; i<=n; i++) cin >> b[i];

    for(int i=1; i<=n; i++){
        for(int j=99; j-a[i]>=0; j--) dp[j] = max(dp[j] , dp[j-a[i]] + b[i]);
    }

    cout << *max_element(dp,dp+100);

}