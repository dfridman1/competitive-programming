# http://www.spoj.com/problems/ABA12C/
# TAGS: dynamic-programming


def buy_apples(n, prices):
    k = len(prices)
    dp = [[-1 for _ in xrange(k+1)] for _ in xrange(n+1)]
    dp[0][0] = 0
    for i in xrange(1, n+1):
        for j in xrange(1, k+1):
            for w, p in enumerate(prices, 1):
                if w > j:
                    break
                if p == -1 or dp[i-1][j-w] == -1:
                    continue
                t = dp[i-1][j-w]+p
                if dp[i][j] != -1:
                    t = min(dp[i][j], t)
                dp[i][j] = t
    amount = -1
    for i in xrange(1, n+1):
        if dp[i][k] != -1:
            amount = min(amount, dp[i][k]) if amount != -1 else dp[i][k]
    return amount


def get_data():
    for _ in xrange(int(raw_input())):
        n, _ = map(int, raw_input().split())
        prices = map(int, raw_input().split())
        yield n, prices


def main():
    for n, prices in get_data():
        print(buy_apples(n, prices))


if __name__ == '__main__':
    main()
