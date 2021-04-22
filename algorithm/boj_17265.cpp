#include <iostream>
#include <string>
using namespace std;

int n , max_dp[6][6], min_dp[6][6];
char m[6][6];
int cal(int a, int b, char alpha){
    if(alpha == '-') return a-b;
    if(alpha == '+') return a+b;
    return a*b;
}
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> m[i][j];
        }
    }
    max_dp[0][0] = min_dp[0][0] = m[0][0]-'0';
    for(int i=1; i<n ;i++){
        if(i%2 != 0) continue;
        min_dp[i][0] = max_dp[i][0] = cal(max_dp[i-2][0] , m[i][0]-'0' , m[i-1][0]);
    }
    for(int i=1; i<n; i++){
        if(i%2 != 0) continue;
        min_dp[0][i] = max_dp[0][i] = cal(max_dp[0][i-2] , m[0][i] -'0' , m[0][i-1]);
    }
    for(int i=1; i<n ;i++){
        for(int j=1; j<n; j++){
            if((i+j)%2 !=0) continue;
            max_dp[i][j] = cal(max_dp[i-1][j-1] , m[i][j] -'0' , m[i-1][j]);
            max_dp[i][j] = max(max_dp[i][j] ,cal(max_dp[i-1][j-1] , m[i][j] -'0' , m[i][j-1]));
            if(i-2 >=0) max_dp[i][j] = max(max_dp[i][j] , cal(max_dp[i-2][j] , m[i][j]-'0' , m[i-1][j]));
            if(j-2 >=0) max_dp[i][j] = max(max_dp[i][j] , cal(max_dp[i][j-2] , m[i][j] -'0' , m[i][j-1]));

            min_dp[i][j] = cal(min_dp[i-1][j-1] , m[i][j] -'0' , m[i-1][j]);
            min_dp[i][j] = min(min_dp[i][j] , cal(min_dp[i-1][j-1] , m[i][j] -'0' , m[i][j-1]));
            if(i-2 >=0) min_dp[i][j] = min(min_dp[i][j] , cal(min_dp[i-2][j] , m[i][j]-'0' , m[i-1][j]));
            if(j-2 >=0) min_dp[i][j] = min(min_dp[i][j] , cal(min_dp[i][j-2] , m[i][j]-'0' , m[i][j-1]));

        }
    }
    cout << max_dp[n-1][n-1] << " " << min_dp[n-1][n-1];
}