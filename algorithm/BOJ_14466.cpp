#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int road[101][101][4];
bool visit[101][101];
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
int n, k, r;
int r1, c1, r2, c2;
vector<pair<int, int>>cow;
bool bfs(int a, int b) {
	int x = cow[a].first;
	int y = cow[a].second;
	memset(visit, false, sizeof(visit));
	queue<pair<int, int>>que;
	que.push({ x,y });
	while (!que.empty()) {
		auto curr = que.front();
		que.pop();

		if (curr.first == cow[b].first && curr.second == cow[b].second) {
			return true;
		}
		if (visit[curr.first][curr.second]) continue;
		visit[curr.first][curr.second] = true;

		for (int i = 0; i < 4; i++) {
			if (road[curr.first][curr.second][i] == true) continue;
			int nx = curr.first + dx[i];
			int ny = curr.second + dy[i];
			if (nx == 0 or nx == n + 1 or ny == 0 or ny == n + 1) continue;
			if (visit[nx][ny] == true) continue;
			que.push({ nx,ny });
		}
	}
	return false;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin >> n >> k >> r;
	memset(road, false, sizeof(road));
	for (int i = 0; i < r; i++) {
		cin >> r1 >> c1 >> r2 >> c2;
		int r1dir = -1;
		int r2dir = -1;
		if (r1 == r2) {
			if (c1 > c2) {
				r1dir = 0;
				r2dir = 2;
			}
			else {
				r1dir = 2;
				r2dir = 0;
			}
		}
		else {
			if (r1 > r2) {
				r1dir = 1;
				r2dir = 3;
			}
			else{
				r1dir = 3;
				r2dir = 1;
			}
		}
		road[r1][c1][r1dir] = road[r2][c2][r2dir] = true;
	}
	for (int i = 0; i < k; i++) {
		cin >> r1 >> c1;
		cow.push_back({ r1,c1 });
	}
	int ret = 0;
	for (int i = 0; i < k; i++) {
		for (int j = i+1; j < k; j++) {
			if (!bfs(i, j)) ret++;
		}
	}
	cout << ret;
}