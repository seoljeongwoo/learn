#include <iostream>
using namespace std;

int dp[2][4005];
char s[4005], t[4005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> s >> t;
    int slen;
    int tlen;
    for(slen =0 ; s[slen] != '\0'; slen++);
    for(tlen =0 ; t[tlen] != '\0'; tlen++);
    int q = 0;
    int ret = 0;
    for(int i=1; i<=slen; i++){
        for(int j=0; j<=tlen;j++) dp[q][j] = 0;
        for(int j=1; j<=tlen; j++){
            if(s[i-1] == t[j-1]) dp[q][j] = dp[1-q][j-1] + 1;
            else dp[q][j] = 0;
            ret = max(ret, dp[q][j]);
        }
        q = 1-q;
    }
    cout << ret;
}