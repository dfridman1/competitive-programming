# http://www.spoj.com/problems/ADAGAME/
# TAGS: dynamic-programming


# NOTE: Time Limit Exceeded (see adagame.cpp)


class Solver:
    def __init__(self):
        self.max_n = 9999
        self.next_numbers = self.precompute()

    def precompute(self):
        next_numbers = []
        for i in xrange(self.max_n+1):
            s = list('%04d' % i)
            xs = []
            for i in xrange(len(s)):
                prev = s[i]
                s[i] = str((int(prev) + 1) % 10)
                xs.append(int(''.join(s)))
            next_numbers.append(xs)
        return next_numbers

    def will_win(self, xs, i, m):
        if m % 2 == 0:
            if i % 2 == 0:
                return any(xs)
            else:
                return all(xs)
        else:
            if i % 2 == 1:
                return any(xs)
            else:
                return all(xs)

    def get_winner(self, N, m):
        dp = [[False for _ in xrange(self.max_n+1)] for _ in xrange(m+1)]
        for i in xrange(N+1, self.max_n+1):
            dp[0][i] = True
        for i in xrange(1, m+1):
            for j in xrange(self.max_n+1):
                dp[i][j] = self.will_win([dp[i-1][next_j] for next_j in self.next_numbers[j]], i, m)
        winner = 'Ada' if dp[m][N] else 'Vinit'
        return winner


def get_data():
    for _ in xrange(int(raw_input())):
        N, m = map(int, raw_input().split())
        yield N, m


def main():
    solver = Solver()
    for N, m in get_data():
        print(solver.get_winner(N, m))


if __name__ == '__main__':
    main()
