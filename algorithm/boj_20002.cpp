#include <iostream>
using namespace std;

int n, a[305][305], ret = -1005;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for(int i=1; i<=n ;i++){
        for(int j=1; j<=n; j++){
            cin >> a[i][j];
            a[i][j] += (a[i-1][j] + a[i][j-1] - a[i-1][j-1]);
        }
    }

    for(int i=1; i<=n ;i++){
        for(int j=1; j<=n; j++){
            int gap = 1;
            while (i-gap >= 0 && j-gap >=0){
                ret = max(ret, a[i][j] - a[i-gap][j] - a[i][j-gap] + a[i-gap][j-gap]);
                gap++;
            }
        }
    }
    cout << ret;


}