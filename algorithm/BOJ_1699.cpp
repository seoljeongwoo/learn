#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int n; cin >> n;
	int ans = 4;
	for (int i = 1; i * i <= n; i++) {
		if (i * i == n) ans = min(ans, 1);
		for (int j = 1; i * i + j * j <= n; j++) {
			if (i * i + j * j == n) ans = min(ans, 2);
			for (int k = 1; i * i + j * j + k * k <= n; k++) {
				if (i * i + j * j + k * k == n) ans = min(ans, 3);
			}
		}
	}
	cout << ans;
}