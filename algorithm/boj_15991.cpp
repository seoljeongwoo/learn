#include <iostream>
using namespace std;

long long dp[100001];
const int mod = 1e9+9;
int tc, n ;
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);

    dp[1] = 1; dp[2] = 2; dp[3] =2; dp[4]=3; dp[5] = 3; dp[6] = 6;
    for(int i=7; i<=100000; i++){
        dp[i] = (dp[i-2] + dp[i-4] + dp[i-6])% mod;
    }
    
    cin >> tc;
    for(int i=0; i<tc; i++){
        cin >> n;
        cout << dp[n] << "\n";
    }

}