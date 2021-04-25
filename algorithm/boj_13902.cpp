#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n , m , a[1005], dp[10005];
vector <int > ans;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    for(int i=0; i<m; i++) {
        cin >> a[i]; ans.push_back(a[i]);
    }
    for(int i=0; i<=n; i++) dp[i] = 1e9;
    dp[0] = 0;
    for(int i=0; i<m; i++){
        for(int j=i+1; j<m; j++){
            ans.push_back(a[i] + a[j]);
        }
    }
    sort(ans.begin() ,ans.end());
    ans.erase(unique(ans.begin(), ans.end()) , ans.end());
    for(int i=0; i<ans.size(); i++){
        for(int j=ans[i]; j<=n; j++){
            dp[j] = min(dp[j] , dp[j-ans[i]] + 1);
        }
    }
    if(dp[n] == 1e9) cout << -1;
    else cout << dp[n];

}