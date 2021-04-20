#include <iostream>
using namespace std;

char s[1005];
int n, dp[1005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    for(int i=0; i<1000; i++) dp[i] = 1e9;
    cin >> n;
    cin >> s;
    dp[0] = 0;
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            if((s[i] == 'B' && s[j] == 'O') || (s[i] =='O' && s[j] == 'J') || (s[i] == 'J' && s[j] == 'B')){
                dp[j] = min(dp[j] , dp[i] + (j-i) * (j-i));
            }
        }
    }
    if (dp[n-1] == 1e9) cout << -1;
    else cout << dp[n-1];
}