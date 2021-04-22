#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

int t[2005][2005] , s;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> s;
    memset(t, -1, sizeof(t));
    queue < pair <int ,int > > que;
    que.push(make_pair(1,0));
    t[1][0] = 0;
    while(!que.empty()){
        pair <int ,int > curr = que.front();
        que.pop();
        if(curr.first == s){
            cout << t[curr.first][curr.second];
            return 0;
        }

        if(curr.first <= 2*s && t[curr.first][curr.first] == -1){
            t[curr.first][curr.first] = t[curr.first][curr.second] + 1;
            que.push(make_pair(curr.first, curr.first));
        }
        if(curr.first + curr.second <= 2*s && t[curr.first + curr.second][curr.second] == -1 ){
            t[curr.first + curr.second][curr.second] = t[curr.first][curr.second] + 1;
            que.push(make_pair(curr.first + curr.second , curr.second));
        }
        if(curr.first-1 > 0 && t[curr.first -1][curr.second] == -1){
            t[curr.first -1][curr.second] = t[curr.first][curr.second] + 1;
            que.push(make_pair(curr.first -1, curr.second));
        }
    }


}