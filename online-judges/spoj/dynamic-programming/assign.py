# http://www.spoj.com/problems/ASSIGN/
# TAGS: dynamic-programming

# NOTE: Time Limit Exceeded (see assign.cpp)


def assign(mat):
    return solve(0, mat, 0, {})


def solve(i, mat, mask, cache):
    if i >= len(mat):
        return 1
    ans = cache.get(mask, None)
    if ans is not None:
        return ans
    ans = 0
    for j in xrange(len(mat)):
        set_bit = 1 << j
        if mat[i][j] == '1' and (mask & set_bit == 0):
            ans += solve(i+1, mat, mask | set_bit, cache)
    cache[mask] = ans
    return ans


def get_data():
    for _ in xrange(int(raw_input())):
        mat = []
        for _ in xrange(int(raw_input())):
            mat.append(raw_input().split())
        yield mat


def main():
    for mat in get_data():
        print(assign(mat))


if __name__ == '__main__':
    main()
