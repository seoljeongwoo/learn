#include <iostream>
#include <vector>
using namespace std;

int dp[11], n, k ,ans;
vector <int > a;
void solve(int s){
    if(s == n){
        ans ++;
        if(ans == k){
            for(int i=0; i<a.size()-1; i++){
                cout << a[i] << "+";
            }
            cout << a[a.size()-1];
            exit(0);
        }
        else{
            return;
        }
    }
    for(int i=1; i<=3; i++){
        if (s+i <=n){
            a.push_back(i);
            solve(s+i);
            a.pop_back();
        }
    }
    return;
}
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    dp[1] = 1; dp[2] = 2; dp[3] = 4;
    cin >> n >> k;
    for(int i=4; i<=n; i++){
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]);
    }
    if(dp[n] < k){
        cout << -1;
        return 0;
    }
    solve(0);
    
}  