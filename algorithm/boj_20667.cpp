#include <iostream>
#include <cstring>
using namespace std;

int n , m, k , cpu, memory , priority , dp[1005][505];
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    memset(dp,-1,sizeof(dp));
    dp[0][0] = 0;
    cin >> n >> m >> k;
    for(int i=0; i<n; i++){
        cin >> cpu >> memory >> priority;
        for(int j=1000; j>=0 ;j--){
            for(int l=500; l>=0;l--){
                if(dp[j][l] != -1){
                    if(j+cpu <= 1000 && l+priority <=500) dp[j+cpu][l+priority] = max(dp[j+cpu][l+priority], dp[j][l] + memory);
                }
            }
        }
    }
    int ret = int(1e9);
    for(int i=m; i<=1000; i++){
        for(int j=0; j<=500; j++){
            if(dp[i][j] >= k) ret = min(ret, j);
        }
    }
    if(ret == int(1e9)) ret = -1;
    cout << ret;
}