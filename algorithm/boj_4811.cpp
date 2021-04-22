#include <iostream>
#include <cstring>
using namespace std;

long long dp[35];
int t;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    dp[0] = 1LL; dp[1] = 1LL; dp[2] = 2LL;
    for(int i=3; i<=30; i++){
        for(int j=0; j<i;j++){
            dp[i] += dp[j]*dp[i-j-1];
        }
    }
    while(true){
        cin >> t;
        if( t==0) break;
        cout << dp[t] << "\n";
    }
}