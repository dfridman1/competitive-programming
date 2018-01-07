# http://www.spoj.com/problems/PARADOX/
# TAGS: graph-theory, number-theory, ad-hoc-1


def paradox(graph, n):
    states = [None] * n
    for i in xrange(n):
        if states[i] is None:
            b, _states = dfs(graph, i, True)
            if b:
                b, _states = dfs(graph, i, False)
            if b:
                return True
            for j, s in _states.items():
                states[j] = s
    return False


def dfs(graph, v, init_state):
    stack = [(v, init_state)]
    states = {}
    while len(stack) > 0:
        v, state = stack.pop()
        prev_state = states.get(v, None)
        if prev_state is not None:
            if prev_state != state:
                return True, {}
            else:
                continue
        states[v] = state
        child, child_state = graph[v]
        if not state:
            child_state = not child_state
        stack.append((child, child_state))
    return False, states


def get_data():
    while True:
        n = int(raw_input())
        if n == 0:
            break
        graph = []
        for _ in xrange(n):
            v, state = raw_input().split()
            graph.append((int(v)-1, state == 'true'))
        yield n, graph


def main():
    for n, graph in get_data():
        print('PARADOX' if paradox(graph, n) else 'NOT PARADOX')


if __name__ == '__main__':
    main()
