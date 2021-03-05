#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
int n, k, w[11][11],dp[11][(1<<11)];
int solve(int x, int v) {
	if (v == (1 << n) - 1) return 0;
	int& ret = dp[x][v];
	if (ret != -1) return ret;
	ret = 1e9;
	for (int i = 0; i < n; i++) {
		if (v & (1 << i))continue;
		ret = min(ret, solve(i, v | (1 << i))+w[x][i]);
	}
	return ret;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> w[i][j];
		}
	}
	for (int q = 0; q < n; q++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				w[i][j] = min(w[i][j], w[i][q] + w[q][j]);
			}
		}
	}
	memset(dp, -1, sizeof(dp));
	cout << solve(k, (1 << k));
}