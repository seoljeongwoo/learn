#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;
unordered_set < string > ust;
string s;
void solve(string ret , int l, int r){
    if( l== 0 && r == s.size()-1){
        ust.insert(ret);
        return;
    }
    if(l > 0){
        string ne = s[l-1] + ret;
        solve(ret + ne , l-1, r);
    }
    if(r <s.size()-1){
        string ne = ret + s[r+1];
        solve(ret + ne , l , r+1);
    }
    return;
}
int main(){
    ios_base:: sync_with_stdio(false);
    cin >> s;
    for(int i=0; i<s.size(); i++){
        string r ="";
        r+=s[i];
        solve( r, i, i);
    }
    cout << ust.size();
}