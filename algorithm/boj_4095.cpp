#include <iostream>
using namespace std;

int n , m,a[1005][1005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    while(true){
        cin >> n >> m;
        if(n==0 && m==0) break;

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                cin >> a[i][j];
            }
        }

        for(int i=1; i<n; i++){
            for(int j=1; j<m; j++){
                if(a[i][j]){
                    a[i][j] = min(a[i-1][j] , min(a[i-1][j-1] , a[i][j-1])) +1;
                }
            }
        }

        int ret =0 ;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++){
                ret = max(ret , a[i][j]);
                a[i][j] = 0;
            }
        }
        cout << ret << "\n";
    }

}