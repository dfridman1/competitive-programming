// http://www.spoj.com/problems/TRT/
// TAGS: dynamic-programming

#include <stdio.h>
#include <vector>


unsigned long long dp[2001][2001];


unsigned long long treat_cows(const std::vector<int> &xs) {
  int n = (int)xs.size();
  for (int i = 0; i < n; i++) {
    dp[i][i] = xs[i]*n;
  }
  for (int l = 2; l <= n; l++) {
    int d = n-l+1;
    for (int i = 0; i <= n-l; i++) {
      int j = i+l-1;
      dp[i][j] = std::max(xs[i]*d + dp[i+1][j], xs[j]*d + dp[i][j-1]);
    }
  }
  return dp[0][n-1];
}


std::vector<int> read_data() {
  int n;
  scanf("%d", &n);
  std::vector<int> xs(n, 0);
  for (int i = 0; i < n; i++) {
    scanf("%d", &xs[i]);
  }
  return xs;
}


int main() {
  std::vector<int> xs = read_data();
  printf("%lld\n", treat_cows(xs));
  return 0;
}