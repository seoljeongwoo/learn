#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

char b[31][31][31];
int v[31][31][31];
struct node{
    int x, y, z;
    node(){}
    node(int _x, int _y, int _z) : x(_x), y(_y), z(_z){}
    
};
node st, des;
int dx[6] = {-1,1,0,0,0,0};
int dy[6] = {0,0,-1,1,0,0};
int dz[6] = {0,0,0,0,-1,1};
int l,r,c;
void bfs(){
    memset(v, -1, sizeof(v));
    queue<node> que;
    que.push(st);
    v[st.x][st.y][st.z] = 0;
    while(!que.empty()){
        node curr = que.front();
        que.pop();
        for(int i=0; i<6; i++){
            int nx = curr.x + dx[i];
            int ny = curr.y + dy[i];
            int nz = curr.z + dz[i];
            if(0<=nx && nx<l && 0<=ny && ny<r && 0<= nz && nz<c){
                if(v[nx][ny][nz] == -1 && b[nx][ny][nz] != '#'){
                    v   [nx][ny][nz] = v[curr.x][curr.y][curr.z] + 1;
                    que.push(node(nx,ny,nz));
                }
            }
        }
    }
    if (v[des.x][des.y][des.z] == -1){
        cout << "Trapped!\n";
    }
    else{
        cout << "Escaped in " << v[des.x][des.y][des.z] << " minute(s).\n";
    }
}
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    while(true){
        cin >> l >> r >> c;
        if(!l) break;
        for(int i=0;i<l;i++) {
            for(int j=0; j<r; j++) {
                for(int k=0;k<c; k++) {
                    cin >> b[i][j][k];
                    if(b[i][j][k] == 'S'){
                        st = node(i,j,k);
                    }
                    else if(b[i][j][k] == 'E'){
                        des = node(i,j,k);
                    }
                }
            }
        }
        bfs();
    }
    return 0;
}