#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector<int>lis;
int n,v;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for(int i=0; i<n; i++){
        cin >> v;
        if(lis.empty()){
            lis.push_back(v);
            continue;
        }
        int idx = lower_bound(lis.begin(), lis.end(), v) - lis.begin();
        if (idx == lis.size()){
            lis.push_back(v);
        }
        else{
            lis[idx] = v;
        }
    }
    cout << lis.size();


}