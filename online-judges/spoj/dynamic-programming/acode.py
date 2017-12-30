# http://www.spoj.com/problems/ACODE/
# TAGS: dynamic-programming


def count_ways(s):
    n = len(s)
    dp = [0] * (n+1)
    dp[0] = 1
    i = 0
    while i < n:
        if i+1 < n and s[i+1] == '0':
            dp[i+1] = 0
            dp[i+2] = dp[i]
            i += 2
        else:
            dp[i+1] = dp[i]
            if i > 0 and s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
            i += 1
    return dp[n]


def get_data():
    while True:
        s = raw_input()
        if s == '0':
            break
        yield s


def main():
    for s in get_data():
        print(count_ways(s))


if __name__ == '__main__':
    main()
