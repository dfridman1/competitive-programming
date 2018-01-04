# http://www.spoj.com/problems/SQRBR/
# TAGS: dynamic-programming


def brackets(n, xs):
    n *= 2
    xs = set(xs)
    dp = [[0 for _ in xrange(n+1)] for _ in xrange(n+1)]
    dp[0][0] = 1
    for i in xrange(1, n+1):
        for j in xrange(1, n+1):
            dp[i][j] = dp[i-1][j-1]
        if i not in xs:
            for j in xrange(n):
                dp[i][j] += dp[i-1][j+1]
    return dp[n][0]


def read_data():
    for _ in xrange(int(raw_input())):
        n, k = map(int, raw_input().split())
        xs = map(int, raw_input().split())
        yield n, xs


def main():
    for n, xs in read_data():
        print(brackets(n, xs))


if __name__ == '__main__':
    main()
