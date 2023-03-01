from collections import defaultdict
from math import inf


# pass topo sorted nodes
# otherwise, nodes are assumed to be named in topo order
def longest_path_dag(g, s, t, nodes=None):
    if nodes is None:
        nodes = sorted(g.keys())
    dp = dict(zip(nodes, [-inf] * len(nodes)))
    dp[0, 0] = 0
    backtrack = dict(zip(nodes, [-1] * len(nodes)))
    start_index = nodes.index(s)
    end_index = nodes.index(t)
    for u in nodes[start_index : end_index + 1]:
        for v, weight in g[u]:
            if dp[u] + weight > dp[v]:
                dp[v] = dp[u] + weight
                backtrack[v] = u

    # solve backtrack path iteratively instead of recursively
    path = []
    current = t
    while current != s:
        path.append(current)
        current = backtrack[current]
        if current == -1:
            return None  # path does not exist from s to t
    path.append(s)
    return dp[t], list(reversed(path))


if __name__ == "__main__":
    s, t = map(int, input().split())
    g = defaultdict(list)
    while True:
        try:
            u, v, weight = map(int, input().split())
            g[u].append((v, weight))
            if v not in g:
                g[v] = []
        except:
            break

    length, path = longest_path_dag(g, s, t)
    print(length)
    print(" ".join(map(str, path)))
