#include <iostream>
#include <vector>
using namespace std;

int n , dp[40005];
const int mod = 123456789;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    vector < int > prime;
    vector < bool > isprime(n+1,true);
    for(int i=2; i <= n; i++){
        if(isprime[i]){
            prime.push_back(i);
            for(int j=i*i; j<=n; j+=i) isprime[j] = false;
        }
    }
    dp[0] = 1;
    for(int i=0; i<prime.size(); i++){
        for(int j= prime[i]; j<=n; j++) {
            dp[j] += dp[j-prime[i]];
            dp[j] %= mod;
        }
    }
    cout << dp[n];

}