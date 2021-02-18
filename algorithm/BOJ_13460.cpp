#include <iostream>
#include <string>
#include <queue>
using namespace std;
struct node {
	int a, b, c, d;
	node(){}
	node(int _a, int _b, int _c, int _d):a(_a),b(_b),c(_c),d(_d){}
};
char Map[10][10];
int visit[10][10][10][10];
int N, M, rx, ry, bx, by, ex, ey;
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };
void input() {
	ios_base::sync_with_stdio(false);
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> Map[i][j];
			if (Map[i][j] == 'R') {
				rx = i; ry = j;
				Map[i][j] = '.';
			}
			else if (Map[i][j] == 'B') {
				bx = i; by = j;
				Map[i][j] = '.';
			}
			else if (Map[i][j] == 'O') {
				ex = i; ey = j;
			}
		}
	}
}
int solve() {
	queue <node> q;
	q.push(node(rx, ry, bx, by));
	visit[rx][ry][bx][by] = 1;

	while (!q.empty()) {
		node curr = q.front();
		q.pop();
		for (int i = 0; i < 4; i++) {
			int next_rx = curr.a + dx[i];
			int next_ry = curr.b + dy[i];
			int next_bx = curr.c + dx[i];
			int next_by = curr.d + dy[i];

			while (Map[next_rx][next_ry] == '.') {
				next_rx += dx[i];
				next_ry += dy[i];
			}

			while (Map[next_bx][next_by] == '.') {
				next_bx += dx[i];
				next_by += dy[i];
			}

			if (Map[next_rx][next_ry] == '#') {
				next_rx -= dx[i];
				next_ry -= dy[i];
			}

			if (Map[next_bx][next_by] == '#') {
				next_bx -= dx[i];
				next_by -= dy[i];
			}

			if (next_rx == next_bx && next_ry == next_by) {
				if (next_rx == ex && next_ry == ey) continue;
				else {
					int r_dist = abs(next_rx - curr.a) + abs(next_ry - curr.b);
					int b_dist = abs(next_bx - curr.c) + abs(next_by - curr.d);
					if (r_dist > b_dist) {
						next_rx -= dx[i];
						next_ry -= dy[i];
					}
					else {
						next_bx -= dx[i];
						next_by -= dy[i];
					}
				}
			}
			else {
				if (next_rx == ex && next_ry == ey) return visit[curr.a][curr.b][curr.c][curr.d];
				else if (next_bx == ex && next_by == ey) continue;
			}
			if (visit[next_rx][next_ry][next_bx][next_by] != 0) continue;
			if (visit[curr.a][curr.b][curr.c][curr.d] == 10) continue;
			q.push(node(next_rx, next_ry, next_bx, next_by));
			visit[next_rx][next_ry][next_bx][next_by] = visit[curr.a][curr.b][curr.c][curr.d] + 1;
		}
	}
	return -1;
}
int main() {
	input();
	cout << solve();
}