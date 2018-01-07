# http://www.spoj.com/problems/INVCNT/
# TAGS: graph-theory, number-theory, shortest-path, sorting, bitmasks


def count_inversions(xs):
    return _count_inversions(xs)[1]


def _count_inversions(xs):
    if len(xs) < 2:
        return xs, 0
    mid = len(xs) >> 1
    l, left = _count_inversions(xs[:mid])
    r, right = _count_inversions(xs[mid:])
    m, cross = merge(l, r)
    return m, left + right + cross


def merge(xs, ys):
    zs = []
    i = j = inv = 0
    while i < len(xs) and j < len(ys):
        if xs[i] > ys[j]:
            inv += len(xs)-i
            zs.append(ys[j])
            j += 1
        else:
            zs.append(xs[i])
            i += 1
    while i < len(xs):
        zs.append(xs[i])
        i += 1
    while j < len(ys):
        zs.append(ys[j])
        j += 1
    return zs, inv


def get_data():
    n = int(raw_input())
    raw_input()
    for _ in xrange(n):
        N = int(raw_input())
        xs = []
        for _ in xrange(N):
            xs.append(int(raw_input()))
        raw_input()
        yield xs


def main():
    for xs in get_data():
        print(count_inversions(xs))


if __name__ == '__main__':
    main()
