#include <iostream>
#include <algorithm>
using namespace std;

int n , a[1005] , dp[1005];
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    
    cin >> n;
    for(int i=1; i<=n; i++) cin >> a[i];
    for(int i=1; i<=n ;i++){
        for(int j=i-1; j>=1; j--){
            if(a[i] < a[j]) dp[i] = max(dp[i], dp[j]);
        }
        dp[i] += a[i];
    }
    cout << *max_element(dp+1, dp+n+1);
    
}