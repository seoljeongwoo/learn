#include <iostream>
#include <cstring>
using namespace std;

int n,a[6] ,b[6];
long long dp[6][6][11][11][11][11][11];

long long solve(int ppre , int pre, int b1, int b2, int b3, int b4, int b5){
    if(b1+b2+b3+b4+b5 ==0) return 1;
    long long &ret = dp[ppre][pre][b1][b2][b3][b4][b5];
    if(ret != -1) return ret;
    ret = 0;
    if(b1){
        if(ppre != 1 && pre!= 1)ret += solve(pre, 1, b1-1,b2,b3,b4,b5);
    }
    if(b2){
        if(ppre != 2 && pre != 2) ret += solve(pre, 2, b1, b2-1, b3, b4, b5);
    }
    if(b3){
        if(ppre != 3 && pre != 3) ret += solve(pre, 3, b1,b2,b3-1,b4,b5);
    }
    if(b4){
        if(ppre != 4 && pre != 4) ret += solve(pre, 4, b1, b2, b3, b4-1, b5);
    }
    if(b5){
        if(ppre != 5 && pre != 5) ret += solve(pre, 5, b1, b2, b3, b4, b5-1);
    }
    return ret;
}
int main(){ 
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    memset(dp,-1,sizeof(dp));
    cin >> n;
    for(int i=1; i<=n ;i++) cin >> a[i];
    cout << solve(0,0,a[1],a[2],a[3],a[4],a[5]);
}