# http://www.spoj.com/problems/ADFRUITS/
# TAGS: lcs, dynamic-programming, backtracking


def fruits(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    xs, ys = [], []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            i -= 1
            j -= 1
            xs.append(i)
            ys.append(j)
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    ans = ''
    start_x, start_y = 0, 0
    for i, j in reversed(zip(xs, ys)):
        ans += s1[start_x:i] + s2[start_y:j] + s1[i]
        start_x = i+1
        start_y = j+1
    ans += s1[start_x:m] + s2[start_y:n]
    return ans


def get_data():
    while True:
        try:
            yield raw_input().split()
        except EOFError:
            break


def main():
    for s1, s2 in get_data():
        print(fruits(s1, s2))


if __name__ == '__main__':
    main()
