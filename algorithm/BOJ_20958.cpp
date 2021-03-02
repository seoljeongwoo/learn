#include <iostream>
#include <vector>
#include <set>
using namespace std;
#define MN 3333
vector<bool>isprime(MN+1, true);
vector<int>prime;
void eratos() {
    isprime[1] = false;
    for (int i = 2; i <= MN; i++) {
        if (isprime[i] == false) continue;
        prime.push_back(i);
        for (int j = i * i; j <= MN; j += i) {
            isprime[j] = false;
        }
    }
}
bool check(vector<int>& v) {
    for (auto& i : v) {
        if (i % 7 != 0) return false;
        i /= 7;
        if (i % 7 == 0) return false;
    }
    return true;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    eratos();
    int N, M; cin >> N >> M;
    vector<int>jackpot(N);
    for (auto& i : jackpot)cin >> i;
    if (!check(jackpot)) {
        cout << "-1";
        return 0;
    }
    int result = 0;
    for (auto p : prime) {
        vector<int>chk(N + M, 0);
        int high = 0;
        for (int i = 0; i < N; i++) {
            int& val = jackpot[i];
            int cnt = 0;
            while (val % p == 0) {
                val /= p;
                cnt++;
            }

            if (high < cnt) {
                result += (cnt - high);
                chk[i + M - 1] = (cnt - high);
                high = cnt;
            }
            high -= chk[i];
        }
    }

    vector<int>chk(N + M, 0);
    set<int>st;
    st.insert(1);
    for (int i = 0; i < N; i++) {
        int val = jackpot[i];
        if (st.find(val) == st.end()) {
            st.insert(val);
            chk[i + M - 1] = val;
            result++;
        }
        if (chk[i] != 0) {
            st.erase(chk[i]);
        }
    }
    cout << result;
}