#include <iostream>
#include <cstring>
using namespace std;

int n, m[1005][1005],dp[1005][1005][3];
int solve(int x, int y, int milk){
    if (x ==n || y==n) return 0;

    int&ret = dp[x][y][milk];
    if(ret != -1) return ret;
    ret = 0;
    if(milk == m[x][y]){
        ret = max(ret, solve(x+1,y,(milk+1)%3) + 1);
        ret = max(ret, solve(x,y+1,(milk+1)%3) + 1);
    }
    ret = max(ret, solve(x+1,y,milk));
    ret = max(ret, solve(x,y+1,milk));
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    memset(dp,-1,sizeof(dp));
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> m[i][j];
        }
    }

    cout << solve(0,0,0);

}