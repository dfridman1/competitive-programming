# http://www.spoj.com/problems/ACTIV/
# TAGS: dynamic-programming, binary-search

from collections import namedtuple


Activity = namedtuple('Activity', 'start end')


def count_ways(activities):
    activities = sorted(activities, key=lambda x: x.end)
    end_times = [x.end for x in activities]
    dp = [0] * (len(activities)+1)
    for i, x in enumerate(activities, 1):
        dp[i] = dp[i-1]+1
        j = bin_search(end_times, x.start)
        if j != -1:
            dp[i] += dp[j+1]
    return dp[len(activities)]


def bin_search(xs, key):
    lo, hi = 0, len(xs)
    while hi-lo > 1:
        mid = (lo+hi) >> 1
        if xs[mid] > key:
            hi = mid
        else:
            lo = mid
    if hi-lo == 1 and xs[lo] <= key:
        return lo
    return -1


def get_activities():
    while True:
        n = int(raw_input())
        if n == -1:
            break
        activities = []
        for _ in xrange(n):
            activities.append(Activity(*map(int, raw_input().split())))
        yield activities


def main():
    for activities in get_activities():
        num_ways = count_ways(activities)
        print(('%08d' % num_ways)[-8:])


if __name__ == '__main__':
    main()
