#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int n , m , s , e , q, u ,v , b;
vector < vector < pair <int ,int > > > edge;
int dist[255][255];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;
    edge.resize(n+1);
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            dist[i][j] = int(1e9);
            if(i==j)dist[i][j] = 0;
        }
    }
    for(int i=0; i<m ;i++){
        cin >> u >> v >> b;
        if(!b){
            dist[u][v] = 0;
            dist[v][u] = 1;
        }
        else{
            dist[u][v] = dist[v][u] = 0;
        }
    }
    for(int k=1; k<=n; k++){
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                if(dist[i][j] > dist[i][k] + dist[k][j]) dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }
    cin >> q;
    for(int i=0; i<q; i++){
        cin >> s >> e;
        cout << dist[s][e] << "\n";
    }
}