#include <iostream>
using namespace std;

int coin[100001] , n;
int main(){
    ios_base:: sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for(int i=1; i<=n; i++){
        coin[i] = i;
        if(i>=2) coin[i] = min(coin[i] , coin[i-2] + 1);
        if(i>=5) coin[i] = min(coin[i] , coin[i-5] + 1);
        if(i>=7) coin[i] = min(coin[i] , coin[i-7] + 1);
    }
    cout << coin[n];

}