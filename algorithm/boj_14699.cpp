#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector < vector < int > > edge;
int n, m, h[5005],u,v , inq[5005] , dp[5005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;
    for(int i=1; i<=n ;i++) cin >> h[i];
    edge.resize(n+1);

    for(int i=0; i<m; i++){
        cin >> u >> v;
        if(h[u] > h[v]){
            inq[v] ++;
            edge[u].push_back(v);
        }
        else{
            inq[u] ++;
            edge[v].push_back(u);
        }
    }
    queue < int > que;
    for(int i=1; i<=n ;i++){
        if(!inq[i]) que.push(i);
    }
    while(!que.empty()){
        int c = que.front();
        que.pop();
        dp[c] ++ ;
        for(int i=0; i<edge[c].size(); i++){
            int nx = edge[c][i];
            inq[nx] --;
            dp[nx] = max(dp[nx] , dp[c]);
            if(!inq[nx]) que.push(nx);
        }
    }
    for(int i=1; i<=n; i++){
        cout << dp[i] << "\n";
    }
}