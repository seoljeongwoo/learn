#include <iostream>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;
#define INF 1e9+1
vector<vector<pair<int, int>>>edge;
bool visit[5001];
int bfs(int k, int v) {
	memset(visit, false, sizeof(visit));
	queue<int>q;
	q.push(v);
	visit[v] = true;
	int ret = 0;
	while (!q.empty()) {
		int curr = q.front();
		q.pop();

		for (auto next : edge[curr]) {
			if (visit[next.first]) continue;
			if (next.second < k) continue;
			visit[next.first] = true;
			q.push(next.first);
			ret++;
		}
	}
	return ret;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int n, q; cin >> n >> q;
	int u, v, r,k;
	edge.resize(n + 1);
	for (int i = 0; i < n - 1; i++) {
		cin >> u >> v >> r;
		edge[u].push_back({ v,r });
		edge[v].push_back({ u,r });
	}
	for (int i = 0; i < q; i++) {
		cin >> k >> v;
		cout << bfs(k, v) << "\n";
	}
}