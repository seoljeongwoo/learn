#include <iostream>
#include <cstring>
using namespace std;

long long dp[15][2005], tc, n,m;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    for(int i=1; i<=2000; i++) dp[1][i] = 1;
    for(int i=2; i<=10; i++){
        for(int j=1; j<=2000; j++){
            for(int k=1; k<=j/2; k++){
                dp[i][j] += dp[i-1][k];
            }
        }
    }
    cin >> tc;
    for(int i=0; i<tc; i++){
        cin >> n >>m;
        long long ret =0;
        for(int j=1; j<=m; j++) ret += dp[n][j];
        cout << ret << "\n";
    }
}