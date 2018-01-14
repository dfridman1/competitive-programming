// http://www.spoj.com/problems/ASSIGN/
// TAGS: dynamic-programming


#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

typedef unsigned long long ll;

ll dp[1 << 20];

ll solve(int i, const vector<vector<bool> > &mat, ll mask) {
    if (i >= mat.size()) return 1;
    ll ans = dp[mask];
    if (ans != -1) return ans;
    ans = 0;
    for (int j = 0; j < mat.size(); j++) {
        ll set_bit = 1ULL << j;
        if (mat[i][j] && ((mask & set_bit) == 0)) {
            ans += solve(i+1, mat, mask | set_bit);
        }
    }
    dp[mask] = ans;
    return ans;
}


int main() {
    int qq;
    cin >> qq;
    while (qq-- > 0) {
        int n;
        cin >> n;
        vector<vector<bool> > mat(n, vector<bool>(n, false));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                char c;
                cin >> c;
                mat[i][j] = (c == '1');
            }
        }
        memset(dp, -1, sizeof dp);
        cout << solve(0, mat, 0) << endl;
    }
    return 0;
}
