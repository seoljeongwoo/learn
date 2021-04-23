#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int n, k , a,b,c,d ,dp[100005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> k;
    cin >> a >> b >> c >> d;
    dp[a] = max(dp[a],b); dp[c] = max(dp[c],d);
    for(int i=1; i<n ;i++){
        cin >> a >> b >> c >> d;
        for(int j=k; j>=0; j--){
            if(dp[j]){
                if(j+a <= k) dp[j+a] = max(dp[j+a] , dp[j] + b);
                if(j+c <= k) dp[j+c] = max(dp[j+c] , dp[j] + d);
                dp[j]=0;
            }
        }
    }
    cout << *max_element(dp,dp+k+1);
}