#include <iostream>
#include <cstring>
using namespace std;

int n , a[2005], dp[2005][2005], m , s,e;
int solve(int l, int r){
    if( l==r ) return 1;
    if( l + 1 == r){
        if(a[l] == a[r]) return 1;
        else return 0;
    }
    int &ret = dp[l][r];
    if(ret != -1) return ret;
    ret = 0;
    if(a[l] == a[r]) ret = solve(l+1,r-1);
    
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    for(int i=1; i<=n ;i++) cin >> a[i];
    memset(dp,-1,sizeof(dp));
    cin >> m;
    for(int i=0; i<m; i++){
        cin >> s >> e;
        cout << solve(s,e) << "\n";
    }
}