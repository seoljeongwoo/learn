#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;
vector<vector<pair<int, int>>>edge;
bool visit[1001][1001];
int n, p, k;
int u, v, w;
bool check(int mid) {
	memset(visit, false, sizeof(visit));
	queue<pair<int, int>>que;
	que.push({ 1,k });
	while (!que.empty()) {
		auto curr = que.front();
		que.pop();
		if (curr.first == n) return true;
		if (visit[curr.first][curr.second]) continue;
		visit[curr.first][curr.second] = true;
		for (auto next : edge[curr.first]) {
			if (next.second > mid) {
				if (curr.second == 0) continue;
				if (visit[next.first][curr.second - 1]) continue;
				que.push({ next.first, curr.second - 1 });
			}
			else {
				if (visit[next.first][curr.second]) continue;
				que.push({ next.first , curr.second });
			}
		}
	}
	return false;
}
int main() {
	cin >> n >> p >> k;
	edge.resize(n + 1);
	for (int i = 0; i < p; i++) {
		cin >> u >> v >> w;
		edge[u].push_back({ v,w });
		edge[v].push_back({ u,w });
	}
	int lo = 0, hi = 1000001;
	int result = -1;
	while (lo <= hi) {
		int mid = (lo + hi) / 2;

		if (check(mid)) {
			result = mid;
			hi = mid-1;
		}
		else {
			lo = mid + 1;
		}
	}
	cout << result;
}