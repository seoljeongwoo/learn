#include <iostream>
#include <cstring>
using namespace std;

// int t,k, a[105][2],dp[105][10005];
// int solve(int c, int p){
//     if( p ==0) return 1;
//     if( c == k) return 0;
//     int &ret = dp[c][p];
//     if(ret !=-1) return ret;
//     ret = solve(c+1,p);
//     for(int i=1; i<=a[c][1]; i++){
//         int v = a[c][0]*i;
//         if(p-v >=0) ret += solve(c+1,p-v);
//     }
//     return ret;
// }
int t,k,a[105][2],dp[2][10005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    // memset(dp, -1, sizeof(dp));
    // cin >> t >> k;
    // for(int i=0; i<k; i++){
    //     cin >> a[i][0] >> a[i][1];
    // }
    // cout << solve(0,t);
    cin >> t >> k;
    for(int i=0; i<k; i++){
        cin >> a[i][0] >> a[i][1];
    }
    for(int i=0; i<=a[0][1]; i++){
        if(a[0][0]*i <= t)dp[0][a[0][0]*i] = 1;
        else break;
    }

    for(int i=1; i<k; i++){
        for(int j=0;j<=t;j++) dp[i%2][j]=0;
        for(int j=0; j<=t; j++){
            if(dp[(i-1)%2][j] ==0 ) continue;
            for(int l =0; l<=a[i][1]; l++){
                if(j+a[i][0]*l <= t) dp[i%2][j+a[i][0]*l] += dp[(i-1)%2][j];
                else break;
            }
        }
    }
    cout << dp[(k-1)%2][t];
}