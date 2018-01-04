# http://www.spoj.com/problems/ROCK/
# TAGS: dynamic-programming


def rock(s):
    n = len(s)
    counts = count_ones(s)
    dp = [0] * (n+1)
    for i in xrange(1, n+1):
        for j in xrange(i):
            t = (counts[j+1][i] > (i-j)//2) * (i-j)
            dp[i] = max(dp[i], t + dp[j])
    return dp[n]


def count_ones(s):
    n = len(s)
    counts = [[0 for _ in xrange(n+1)] for _ in xrange(n+1)]
    for i in xrange(1, n+1):
        for j in xrange(i, n+1):
            counts[i][j] += counts[i][j-1] + (s[j-1] == '1')
    return counts


def read_data():
    for _ in xrange(int(raw_input())):
        raw_input()
        yield raw_input()


def main():
    for s in read_data():
        print(rock(s))


if __name__ == '__main__':
    main()
