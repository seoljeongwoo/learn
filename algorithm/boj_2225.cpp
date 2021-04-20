#include <iostream>
#include <cstring>
using namespace std;
const int mod = 1e9;
int N , K , dp[205][205];

int solve(int n, int k){
    if(n==0 || k==1) return 1;
    int &ret = dp[n][k];
    if( ret != -1) return ret;
    ret = 0;
    for(int i=0; i<=n; i++) {
        ret+= solve(n-i,k-1);
        ret %= mod;
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    memset(dp,-1,sizeof(dp));
    cin >> N >> K;
    cout << solve(N,K);

}