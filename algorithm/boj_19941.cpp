#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n,k; cin>> n>> k;
    string s; cin >> s;

    vector<int>human, burger, pick;
    for(int i=0 ; i<n; i++){
        if(s[i] == 'H') burger.push_back(i);
        else human.push_back(i);
    }
    int burger_index;
    for(int i=0; i<human.size(); i++){
        if(pick.size() == 0) burger_index = -1;
        else burger_index = pick.back();

        for(int j=burger_index + 1; j<burger.size(); j++){
            if(burger[j] > human[i] + k) break;
            if(abs(burger[j] - human[i]) <= k){
                pick.push_back(j);
                break;
            }
        }
    }
    cout << pick.size();
}