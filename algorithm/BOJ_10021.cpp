#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
int n, c,x,y;
int parent[2001];
vector<pair<int, int>>point;
int dist(int a, int b) {
	int temp = (point[a].first - point[b].first) * (point[a].first - point[b].first);
	temp += ((point[a].second - point[b].second) * (point[a].second - point[b].second));
	return temp;
}
int find(int u) {
	if (u == parent[u]) return u;
	return parent[u] = find(parent[u]);
}
void merge(int u, int v) {
	u = find(u);
	v = find(v);
	parent[u] = v;
}
int main() {
	cin >> n >> c;
	for (int i = 0; i < n; i++) {
		parent[i] = i;
		cin >> x >> y;
		point.push_back({ x,y });
	}
	priority_queue < pair<int, pair<int, int>>>pq;
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			pq.push({ -dist(i,j),{i,j} });
		}
	}
	int pick = 0;
	int result = 0;
	while (!pq.empty()) {
		if (pick == n - 1) break;
		auto curr = pq.top();
		pq.pop();
		if (-curr.first < c) continue;
		if (find(curr.second.first) == find(curr.second.second)) continue;
		merge(curr.second.first, curr.second.second);
		pick++; result += (-curr.first);
	}
	if (pick == n - 1) cout << result;
	else cout << "-1";
}