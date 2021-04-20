#include <iostream>
using namespace std;

int n, m, a[1030][1030], lx, rx , ly , ry , k;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            cin >> a[i][j];
        }
    }
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            a[i][j] = (a[i][j] + a[i-1][j] + a[i][j-1] - a[i-1][j-1]);
        }
    }
    cin >> k;
    for(int i=0; i<k; i++){
        cin >> lx >> ly >> rx >> ry;
        cout << a[rx][ry] - a[lx-1][ry] - a[rx][ly-1] + a[lx-1][ly-1] << "\n";
    }
}