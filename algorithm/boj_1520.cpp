#include <iostream>
#include <cstring>
using namespace std;

int n, m, a[505][505], dp[505][505],dx[4] = {-1,0,1,0} , dy[4] = {0,1,0,-1};
int solve(int x, int y){
    if( x== n &&  y==m) return 1;
    int &ret= dp[x][y];
    if(ret!=-1) return ret;
    ret = 0;
    for(int i=0; i<4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0<nx&& nx<= n && 0<ny && ny<=m && a[x][y] > a[nx][ny]){
            ret += solve(nx,ny);
        }
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    memset(dp,-1,sizeof(dp));
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            cin >> a[i][j];
        }
    }
    cout << solve(1,1);

}