// http://www.spoj.com/problems/BADXOR/
// TAGS: dynamic-programming


#include <iostream>
#include <cstring>
#include <vector>

#define MOD 100000007
#define LIMIT 1024

using namespace std;

typedef unsigned long long ll;

ll dp[1001][LIMIT];
bool mask[LIMIT];


ll badxor(const vector<int>&xs, const vector<int>&ys) {
    int n = (int)xs.size();
    dp[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        int x = xs[i-1];
        for (int j = 0; j < LIMIT; j++) {
            dp[i][j] += dp[i-1][j];
            dp[i][j] %= MOD;
            int t = x ^ j;
            dp[i][t] += dp[i-1][j];
            dp[i][t] %= MOD;
        }
    }
    ll ans = 0;
    for (int y : ys) mask[y] = true;
    for (int i = 0; i < LIMIT; i++) if (!mask[i]) ans = (ans + dp[n][i]) % MOD;
    return ans;
}


int main() {
    int qq;
    cin >> qq;
    for (int i = 1; i <= qq; i++) {
        int n, m;
        cin >> n >> m;
        vector<int>xs(n);
        for (int j = 0; j < n; j++) cin >> xs[j];
        vector<int>ys(m);
        for (int j = 0; j < m; j++) cin >> ys[j];
        memset(dp, 0, sizeof dp);
        memset(mask, false, sizeof mask);
        cout << "Case " << i << ": " << badxor(xs, ys) << endl;
    }
    return 0;
}
