#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int a,b,ret;
int dx[8] = {-1,-1,0,1,1,1,0,-1};
int dy[8] = {0,-1,-1,-1,0,1,1,1};
bool range_check(int x, int y){
    return 0<=x && x<4 && 0<=y && y<4;
}

void solve(int shark_x, int shark_y, int shark_dir, int eating, vector < vector < int > > m, vector < bool > alive, vector < vector < int > > fish){
    if(shark_x == 5 && shark_y == 5){
        ret = max(ret, eating);
        return;
    }
    // 물고기
    for(int i=1; i<=16; i++){
        if(alive[i] == false) continue;
        int curr_x = fish[0][i];
        int curr_y = fish[1][i];
        int curr_dir = fish[2][i];
        for(int j=0; j<8; j++){
            int next_dir = (curr_dir + j)%8;
            int next_x = curr_x + dx[next_dir];
            int next_y = curr_y + dy[next_dir];
            if(range_check(next_x,next_y) == false) continue;
            if(m[next_x][next_y] == 0) continue;
            if(m[next_x][next_y] == -1){    // 빈공간
                m[next_x][next_y] = i;
                m[curr_x][curr_y] = -1;
                fish[0][i] = next_x;
                fish[1][i] = next_y;
                fish[2][i] = next_dir;
                break;
            }
            else{
                int temp = m[next_x][next_y];
                m[next_x][next_y] = i;
                fish[0][i] = next_x;
                fish[1][i] = next_y;
                fish[2][i] = next_dir;
                m[curr_x][curr_y] = temp;
                fish[0][temp] = curr_x;
                fish[1][temp] = curr_y;
                break;
            }
        }
    }
    // 상어
    for(int i=1; ; i++){
        int next_shark_x = shark_x + dx[shark_dir]*i;
        int next_shark_y = shark_y + dy[shark_dir]*i;
        if (range_check(next_shark_x, next_shark_y) == false){
            solve(5,5,0,eating, m, alive, fish);
            break;
        }
        else if(m[next_shark_x][next_shark_y] == -1){
            continue;
        }
        else{
            int eat_num = m[next_shark_x][next_shark_y];
            alive[eat_num]= false;
            m[shark_x][shark_y] = -1;
            m[next_shark_x][next_shark_y] = 0;
            solve(next_shark_x, next_shark_y, fish[2][eat_num] , eating + eat_num , m,alive,fish);
            m[next_shark_x][next_shark_y] = eat_num;
            m[shark_x][shark_y] = 0;
            alive[eat_num]= true;
        }
    }
    return;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    vector < vector < int > > m(4,vector < int > (4,0));
    vector < bool > alive(17,true);
    vector < vector < int > > fish(4, vector <int > (17, 0));
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            cin >> a >> b;
            b-=1;
            fish[0][a] = i;
            fish[1][a] = j;
            fish[2][a] = b;
            m[i][j] = a;
        }
    }
    int first_eat = m[0][0];
    m[0][0] = 0;
    alive[first_eat] = false;
    solve(0,0,fish[2][first_eat],first_eat,m,alive,fish);
    cout << ret;
}