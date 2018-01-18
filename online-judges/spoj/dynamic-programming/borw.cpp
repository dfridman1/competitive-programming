// http://www.spoj.com/problems/BORW/
// TAGS: dynamic-programming


#include <iostream>
#include <algorithm>
#include <cstring>
#include <map>
#include <vector>


using namespace std;


typedef vector<int> vi;


int dp[205][205][205];


int solve(int i, int j, int k, const vi &xs) {
    if (k >= xs.size()) return 0;
    if (dp[i+1][j+1][k] != -1) return dp[i+1][j+1][k];
    int ans = 1 + solve(i, j, k+1, xs);
    if (i == -1 || xs[k] > xs[i]) ans = min(ans, solve(k, j, k+1, xs));
    if (j == -1 || xs[k] < xs[j]) ans = min(ans, solve(i, k, k+1, xs));
    return dp[i+1][j+1][k] = ans;
}


int bowr(const vi &xs) {
    return solve(-1, -1, 0, xs);
}


int main() {
    int n;
    while (1) {
        scanf("%d", &n);
        if (n == -1) break;
        vi xs(n);
        for (int i = 0; i < n; i++) scanf("%d", &xs[i]);
        memset(dp, -1, sizeof dp);
        printf("%d\n", bowr(xs));
    }
    return 0;
}
