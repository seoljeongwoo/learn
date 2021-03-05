#include <vector>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int R, C, N;
string M[101];
int shoot_height[101];
int v[101][101], dx[4] = { -1,0,1,0 }, dy[4] = { 0,1,0,-1 };
vector<vector<pair<int, int>>>group;
vector<int>group_move;
vector<pair<int, int>>tmp;

bool shoot(int h, int mod) {
	if (mod == 0) {
		for (int i = 0; i < C; i++) {
			if (M[h][i] == 'x') {
				M[h][i] = '.';
				return true;
			}
		}
	}
	else {
		for (int i = C - 1; i >= 0; i--) {
			if (M[h][i] == 'x') {
				M[h][i] = '.';
				return true;
			}
		}
	}
	return false;
}
void dfs(int x, int y, int gsize) {
	v[x][y] = gsize;
	tmp.push_back({ x,y });
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx == -1 || nx == R || ny == -1 || ny == C || v[nx][ny] != -1 || M[nx][ny] == '.') continue;
		dfs(nx, ny, gsize);
	}
	return;
}
void solve() {
	for (int pick = 0; pick < N; pick++) {
		if (!shoot(R - shoot_height[pick], pick % 2)) continue;

		group.clear();
		memset(v, -1, sizeof(v));
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (M[i][j] == 'x' && v[i][j] == -1) {
					tmp.clear();
					dfs(i, j, group.size());
					group.push_back(tmp);
				}
			}
		}
		group_move.clear();
		group_move.resize(group.size() , 101);
		if (group.size() == 1) continue;
		for (int i = 0; i < group.size(); i++) {
			for (int j = 0; j < group[i].size(); j++) {
				int x = group[i][j].first;
				int y = group[i][j].second;
				int move_x = x + 1;
				if (move_x == R || (move_x<R && v[move_x][y]!=-1 && v[x][y] !=v[move_x][y])) {
					group_move[i] = 0;
					break;
				}
				if (move_x < R && v[x][y] == v[move_x][y]) continue;
				while (move_x < R && v[move_x][y] == -1) move_x++;
				if (move_x < R && v[move_x][y] == v[x][y]) continue;
				group_move[i] = min(group_move[i], move_x - x - 1);
			}
		}

		for (int i = 0; i < group.size(); i++) {
			if (group_move[i] == 0 || group_move[i] == 101) continue;
			for (int j = 0; j < group[i].size(); j++) {
				int x = group[i][j].first;
				int y = group[i][j].second;
				M[x][y] = '.';
			}
			for (int j = 0; j < group[i].size(); j++) {
				int x = group[i][j].first;
				int y = group[i][j].second;
				M[x + group_move[i]][y] = 'x';
			}
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	cin >> R >> C;
	for (int i = 0; i < R; i++) {
		cin >> M[i];
	}
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> shoot_height[i];
	}
	solve();
	for (int i = 0; i < R; i++) {
		cout << M[i] << "\n";
	}
}