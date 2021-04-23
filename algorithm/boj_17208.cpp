#include <iostream>
using namespace std;

int n , m , k, dp[305][305] ,x ,y ;
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m >> k;
    for(int i=1; i<=n; i++){
        cin >> x >> y;
        for(int j=m; j>=x; j--){
            for (int l = k; l>=y; l--){
                dp[j][l] = max(dp[j][l] , dp[j-x][l-y] + 1);
            }
        }
    }
    cout << dp[m][k];
}