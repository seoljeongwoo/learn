#include <iostream>
#include <cstring>
using namespace std;

int m, n , a[105], dp[105][55] , d;
int solve(int p,int c){
    if (p > n) return 0;
    int &ret = dp[p][c];
    if (ret != -1) return ret;
    if(a[p]) {
        ret = solve(p+1,c);
        return ret;
    }
    ret = solve(p+1,c) + 10000;
    ret = min(ret, solve(p+3,c+1) + 25000);
    ret = min(ret, solve(p+5,c+2) + 37000);
    if(c>= 3) ret = min(ret, solve(p+1, c-3));
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    memset(dp,-1,sizeof(dp));
    cin >> n >> m;
    for(int i=0; i<m; i++){
        cin >> d;
        a[d] = 1;
    }
    cout << solve(1,0);
}