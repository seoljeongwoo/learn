#include <iostream>
#include <string>
#include <cstring>
using namespace std;

string magic, angel, devil;
int dp[2][105][25];
int solve(int turn, int index, int magic_cnt){
    if( index == angel.size()){
        if(magic_cnt == magic.size()) return 1;
        else return 0;
    }
    int &ret = dp[turn][index][magic_cnt];
    if(ret != -1) return ret;

    ret = solve(turn, index + 1, magic_cnt);

    if(magic_cnt != magic.size()){
        if(turn ==0 ){  //angel
            if(angel[index] == magic[magic_cnt]) ret += solve(1-turn , index+1, magic_cnt +1);
        }
        else{
            if(devil[index] == magic[magic_cnt]) ret += solve(1-turn, index+1, magic_cnt +1);
        }
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> magic >> devil >> angel;
    memset(dp,-1,sizeof(dp));

    cout << solve(0,0,0)  + solve(1,0,0);

}