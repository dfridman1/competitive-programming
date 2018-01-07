# http://www.spoj.com/problems/BUGLIFE/
# TAGS: graph-theory, graph, dfs


from collections import defaultdict


def buglife(graph, n):
    sex = [None] * n
    for i in xrange(n):
        if sex[i] is None:
            if dfs(i, graph, sex):
                return True
    return False


def dfs(v, graph, sex):
    stack = [(v, 0)]
    while len(stack) > 0:
        v, s = stack.pop()
        if sex[v] is not None:
            if sex[v] != s:
                return True
            else:
                continue
        sex[v] = s
        for child in graph[v]:
            stack.append((child, 1-s))
    return False


def get_data():
    for _ in xrange(int(raw_input())):
        n, k = map(int, raw_input().split())
        graph = defaultdict(list)
        for _ in xrange(k):
            u, v = map(int, raw_input().split())
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        yield graph, n


def main():
    for i, (graph, n) in enumerate(get_data(), 1):
        print('Scenario #{}:'.format(i))
        print('Suspicious bugs found!' if buglife(graph, n) else 'No suspicious bugs found!')


if __name__ == '__main__':
    main()
