# http://www.spoj.com/problems/KNAPSACK/


from collections import namedtuple

Item = namedtuple('Item', 'value weight')


def knapsack(S, items):
    n = len(items)
    dp = [[-1 for _ in xrange(S+1)] for _ in xrange(n+1)]
    dp[0][0] = 0
    for i, item in enumerate(items, 1):
        for w in xrange(S+1):
            dp[i][w] = dp[i-1][w]
            if w >= item.weight:
                t = dp[i-1][w-item.weight]
                if t != -1:
                    dp[i][w] = max(dp[i][w], item.value + t)
    return max(dp[n])


def read_data():
    S, N = map(int, raw_input().split())
    items = []
    for _ in xrange(N):
        weight, value = map(int, raw_input().split())
        items.append(Item(value, weight))
    return S, items


def main():
    S, items = read_data()
    print(knapsack(S, items))


if __name__ == '__main__':
    main()
