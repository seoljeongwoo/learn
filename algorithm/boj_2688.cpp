#include <iostream>
using namespace std;

int t , n
long long dp[75][10];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    for(int i=0; i<10; i++) dp[1][i] = 1LL;
    for(int i=2; i<=64; i++){
        for(int j=0; j<10; j++){
            for(int k=j; k<10; k++){
                dp[i][j] += dp[i-1][k];
            }
        }
    }
    for(int i=1; i<=64; i++){
        for(int j=1; j<10; j++) dp[i][j] += dp[i][j-1];
    }

    cin >> t;
    for(int i=0; i<t; i++){
        cin >> n;
        cout << dp[n][9] << "\n";
    }
}