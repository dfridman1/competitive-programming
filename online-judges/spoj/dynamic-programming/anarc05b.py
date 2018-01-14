# http://www.spoj.com/problems/ANARC05B/
# TAGS: dynamic-programming, binary-search



def anarc(xs, ys):
    ans = curr_x = curr_y = i = j = 0
    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            curr_x += xs[i]
            i += 1
        elif xs[i] > ys[j]:
            curr_y += ys[j]
            j += 1
        else:
            ans += max(curr_x, curr_y) + xs[i]
            curr_x = curr_y = 0
            i += 1
            j += 1
    while i < len(xs):
        curr_x += xs[i]
        i += 1
    while j < len(ys):
        curr_y += ys[j]
        j += 1
    ans += max(curr_x, curr_y)
    return ans


def get_data():
    while True:
        xs = map(int, raw_input().split())
        n, xs = xs[0], xs[1:]
        if n == 0:
            break
        ys = map(int, raw_input().split())[1:]
        yield xs, ys


def main():
    for xs, ys in get_data():
        print(anarc(xs, ys))


if __name__ == '__main__':
    main()
