#include <iostream>
using namespace std;

int n,a[35],dp[2][15005],q,p;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for(int i=1; i<=n; i++) cin >> a[i];
    int t =0;
    dp[1][0] = 1;
    for(int i=1; i<=n; i++){
        for(int j=0; j<=15000; j++) dp[t][j] = 0;
        for(int j=0; j<=15000; j++) {
            if(dp[1-t][j]){
                dp[t][j] = 1;
                if(j + a[i] <= 15000) dp[t][j+a[i]] = 1;
                if(j - a[i] >=0) dp[t][j-a[i]] = 1;
                if(a[i] - j >=0) dp[t][a[i] - j] = 1;
            }
        }
        t = 1-t;
    }
    cin >> q;
    for(int i=0; i<q; i++){
        cin >> p;
        if(p > 15000 || dp[1-t][p]==0) cout << "N ";
        else cout << "Y "; 
    }
}