#include <iostream>
#include <vector>
using namespace std;
int n;
vector<pair<int, int>>teacher;
vector<pair<int, int>>student;
vector<pair<int, int>>emp;
char board[7][7];
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };
bool range_check(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < n;
}
bool check() {
	for (int i = 0; i < teacher.size(); i++) {
		int x = teacher[i].first;
		int y = teacher[i].second;
		for (int j = 0; j < 4; j++) {
			int nx = x + dx[j];
			int ny = y + dy[j];
			while (true) {
				if (!range_check(nx, ny)) break;
				if (board[nx][ny] == 'T') break;
				if (board[nx][ny] == 'O')break;
				if (board[nx][ny] == 'S') return false;
				nx += dx[j];
				ny += dy[j];
			}
		}
	}
	return true;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> board[i][j];
			if (board[i][j] == 'T') teacher.push_back({ i,j });
			else if (board[i][j] == 'S') student.push_back({ i,j });
			else emp.push_back({ i,j });
		}
	}
	bool ok = false;
	for (int i = 0; i < emp.size(); i++) {
		board[emp[i].first][emp[i].second] = 'O';
		for (int j = i+1; j < emp.size(); j++) {
			board[emp[j].first][emp[j].second] = 'O';
			for (int k = j + 1; k < emp.size(); k++) {
				board[emp[k].first][emp[k].second] = 'O';
				ok |= check();
				if (ok) break;
				board[emp[k].first][emp[k].second] = 'X';
			}
			if (ok)break;
			board[emp[j].first][emp[j].second] = 'X';
		}
		if (ok)break;
		board[emp[i].first][emp[i].second] = 'X';
	}
	if (ok) cout << "YES";
	else cout << "NO";
}