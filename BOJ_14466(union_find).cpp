#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

bool ok[101][101][4],v[101][101];
int p[101 * 101],dx[4] = { 0,-1,0,1 },dy[4] = { -1,0,1,0 };
int n, k, r,r1, c1, r2, c2;
int find(int u) {
	if (u == p[u]) return u;
	return p[u] = find(p[u]);
}
vector<pair<int, int>>cow;
void merge(int x, int y) {
	x = find(x);
	y = find(y);
	p[x] = y;
}
void dfs(int x, int y, int z) {
	merge(x * 101 + y, z);
	v[x][y] = true;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx == 0 || nx == n + 1 || ny == 0 || ny == n + 1 || v[nx][ny] || !ok[x][y][i]) continue;
		dfs(nx, ny, z);
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin >> n >> k >> r;
	memset(ok, true, sizeof(ok));
	for (int i = 0; i < r; i++) {
		cin >> r1 >> c1 >> r2 >> c2;
		if (r1 + 1 == r2) ok[r1][c1][3] = ok[r2][c2][1] = false;
		else if (r1 - 1 == r2) ok[r1][c1][1] = ok[r2][c2][3] = false;
		else if (c1 + 1 == c2) ok[r1][c1][2] = ok[r2][c2][0] = false;
		else ok[r1][c1][0] = ok[r2][c2][2] = false;
	}
	for (int i = 0; i < 101 * 101; i++) p[i] = i;
	memset(v, false, sizeof(v));
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (!v[i][j]) dfs(i, j, i * 101 + j);
		}
	}
	int ret = 0;
	for (int i = 0; i < k; i++) {
		cin >> r1 >> c1;
		cow.push_back({ r1,c1 });
		for (int j = 0; j < i; j++) {
			if (find(101 * cow[i].first + cow[i].second) != find(101 * cow[j].first + cow[j].second)) {
				ret++;
			}
		}
	}
	cout << ret;
}