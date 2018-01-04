# http://www.spoj.com/problems/TRT/
# TAGS: dynamic-programming

# NOTE: Time Limit Exceeded (see trt.cpp)


def treat_cows(xs):
    n = len(xs)
    get_age = lambda l: n-l+1
    dp = [[float('-inf') for _ in xrange(n)] for _ in xrange(n)]
    d = get_age(1)
    for i in xrange(n):
        dp[i][i] = d*xs[i]
    for l in xrange(2, n+1):
        d = get_age(l)
        for i in xrange(n-l+1):
            j = i+l-1
            dp[i][j] = max(
                d*xs[i] + dp[i+1][j],
                d*xs[j] + dp[i][j-1]
            )
    return dp[0][n-1]


def get_data():
    n = int(raw_input())
    return [int(raw_input()) for _ in xrange(n)]


def main():
    xs = get_data()
    print(treat_cows(xs))


if __name__ == '__main__':
    main()
