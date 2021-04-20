#include <iostream>
using namespace std;

int n, a[205], dp[205];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for(int i=0; i<n; i++) cin >> a[i];

    for(int i=0; i<n; i++){
        for(int j=0; j<i; j++){
            if(a[i] > a[j]){
                dp[i] = max(dp[i], dp[j]+1);
            }
        }
    }
    int mn = 0;
    for(int i=0; i<n ; i++){
        mn = max(mn , dp[i] + 1);
    }
    cout << n - mn;
}