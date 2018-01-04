# http://www.spoj.com/problems/TWENDS/
# TAGS: dynamic-programming


def two_ends(scores):
    n = len(scores)
    dp = [[float('-inf') for _ in xrange(n)] for _ in xrange(n)]
    for i in xrange(n-1):
        dp[i][i+1] = abs(scores[i]-scores[i+1])
    for l in xrange(4, n+1, 2):
        for i in xrange(n-l+1):
            j = i+l-1
            t = scores[i]
            if scores[i+1] >= scores[j]:
                t = t-scores[i+1]+dp[i+2][j]
            else:
                t = t-scores[j]+dp[i+1][j-1]
            dp[i][j] = max(dp[i][j], t)
            t = scores[j]
            if scores[i] >= scores[j-1]:
                t = t-scores[i]+dp[i+1][j-1]
            else:
                t = t-scores[j-1]+dp[i][j-2]
            dp[i][j] = max(dp[i][j], t)
    return dp[0][n-1]


def get_data():
    while True:
        xs = map(int, raw_input().split())
        n, scores = xs[0], xs[1:]
        if n == 0:
            break
        yield scores


def main():
    for i, scores in enumerate(get_data(), 1):
        diff = two_ends(scores)
        print('In game {}, the greedy strategy might lose by as many as {} points.'.format(i, diff))


if __name__ == '__main__':
    main()
