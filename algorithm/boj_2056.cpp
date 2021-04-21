#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n , t[10005] , c, u , inq[10005] , dp[10005];
vector < vector < int > > edge;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(0);

    cin >> n;
    edge.resize(n+1);
    for(int i=1; i<=n; i++){
        cin >> t[i] >> c;
        for(int j=0; j<c; j++){
            cin >> u;
            edge[u].push_back(i);
            inq[i]++;
        }
    }

    queue <int > que;
    for(int i=1; i<=n; i++){
        if(inq[i] == 0) {
            que.push(i);
        }
    }

    while(!que.empty()){
        int curr= que.front();
        que.pop();
        dp[curr] += t[curr];
        for(int i=0 ; i<edge[curr].size(); i++){
            int nx = edge[curr][i];
            dp[nx] = max(dp[nx], dp[curr]);
            inq[nx] --;
            if(inq[nx] ==0) que.push(nx);
        }
    }
    cout << *max_element(dp+1,dp+n+1);
}