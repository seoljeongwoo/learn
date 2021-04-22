#include <iostream>
#include <vector>
using namespace std;
const int gap = 300000;
int n , a[5005], dp[600005];
vector <int > ans;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    for(int i=0; i<n; i++) cin >> a[i];

    int ret =0 ;
    for(int i=0; i<n; i++){
        for(int j=i-1;j>=0; j--){
            if(dp[a[i] - a[j]+gap]){
                ret ++;break;
            }
        }
        for(int j=i; j>=0; j--){
            dp[a[i] + a[j] + gap] = 1;
        }
    }
    cout << ret;
}