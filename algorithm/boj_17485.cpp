#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int n , m , dp[1005][1005][4], a[1005][1005];
int dx[3] = {1,1,1};
int dy[3] = {-1,0,1};
bool range_check(int cy){
    return 0<= cy && cy <m;
}
int solve(int x, int y, int prev){
    if (x == n) return 0;
    int &ret = dp[x][y][prev];
    if(ret !=-1) return ret;
    ret = int(1e9);
    for(int i=0; i<3; i++){
        if(prev == i) continue;
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(range_check(ny) == false) continue;
        ret =min(ret, solve(nx, ny, i) + a[x][y]);
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    memset(dp,-1,sizeof(dp));
    for(int i=0; i<n ;i++){
        for(int j=0; j<m; j++){
            cin >> a[i][j];
        }
    }
    int ret = int(1e9);
    for(int i=0; i<m; i++){
        ret = min(ret, solve(0,i,3));
    }
    cout << ret;

}