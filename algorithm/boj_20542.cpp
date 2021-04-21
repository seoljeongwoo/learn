#include <iostream>
#include <vector>
using namespace std;

int n , m;
char a[1000005], b[1000005];
vector < vector < int > > dp;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    cin >> a;
    cin >> b;
    dp.resize(n+1, vector<int>(m+1,0));
    for(int i=0; i<=n; i++) dp[i][0] = i;
    for(int i=0; i<=m; i++) dp[0][i] = i;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            if(a[i-1] == 'i' && (b[j-1] == 'i' || b[j-1] == 'j' || b[j-1] == 'l')){
                dp[i][j] = dp[i-1][j-1];
            }
            else if(a[i-1] == 'v' && (b[j-1] == 'v' || b[j-1] == 'w')){
                dp[i][j] = dp[i-1][j-1];
            }
            else if(a[i-1] == b[j-1]) dp[i][j] = dp[i-1][j-1];
            else dp[i][j] = min(dp[i-1][j-1] , min(dp[i-1][j], dp[i][j-1])) + 1;
        }
    }
    cout << dp[n][m];
}