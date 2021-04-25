#include <iostream>
#include <cstring>

using namespace std;

int n ,m , item, obs, a[105][105], dp[105][105][205], u , v;
int solve(int x, int y, int get){
    if(a[x][y] == 2) return 0;
    if( x== n && y == m){
        if(get == 0) return 1;
        else return 0;
    }
    int &ret = dp[x][y][get];
    if( ret != -1) return ret;
    ret = 0;
    if(a[x][y] == 1) get--;
    if(x+1 <=n) ret += solve(x+1,y,get);
    if(y+1 <=m) ret += solve(x,y+1,get);
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    memset(dp,-1,sizeof(dp));
    cin >> n >> m >> item >> obs;
    if(n+m-1 < item){
        cout << 0;
        return 0;
    }
    for(int i=0; i<item;i++){
        cin >> u >> v;
        a[u][v] = 1;
    }
    for(int i=0; i<obs; i++){
        cin >> u >> v;
        a[u][v] = 2;
    }
    cout << solve(1,1,item);
}