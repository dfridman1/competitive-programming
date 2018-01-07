# http://www.spoj.com/problems/ANARC08G/
# TAGS: graph-theory, number-theory


def anarc(mat):
    N = len(mat)
    balances = [0 for _ in xrange(N)]
    for i in xrange(N):
        for j in xrange(N):
            if mat[i][j] > 0:
                balances[i] -= mat[i][j]
                balances[j] += mat[i][j]
    return balances


def get_data():
    while True:
        N = int(raw_input())
        if N == 0:
            break
        mat = []
        for _ in xrange(N):
            mat.append(map(int, raw_input().split()))
        yield mat


def main():
    for i, mat in enumerate(get_data(), 1):
        before = sum(map(sum, mat))
        balances = anarc(mat)
        after = sum([x for x in balances if x > 0])
        print('{}. {} {}'.format(i, before, after))


if __name__ == '__main__':
    main()
