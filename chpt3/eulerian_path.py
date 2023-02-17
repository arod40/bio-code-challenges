from eulerian_cycle import eulerian_cycle
from collections import defaultdict

# This method is convert back from the cycle to the actual path
def collect_eulerian_path(cycle, start_node, end_node):
    for i in range(len(cycle) - 1):
        if cycle[i] == end_node and cycle[i + 1] == start_node:
            return cycle[i + 1 : -1] + cycle[: i + 1]


def eulerian_path(g):
    # Compute in and out degrees
    indegrees = {v: 0 for v in g}
    outdegrees = {v: 0 for v in g}

    for v in g:
        for w in g[v]:
            indegrees[w] += 1
            outdegrees[v] += 1

    # Find nodes that start and end the eulerian path
    for v in g:
        if outdegrees[v] > indegrees[v]:
            start_node = v
        if indegrees[v] > outdegrees[v]:
            end_node = v

    g[end_node].append(start_node)

    cycle = eulerian_cycle(g)
    return collect_eulerian_path(cycle, start_node, end_node)


if __name__ == "__main__":
    from pathlib import Path

    lines = Path("dataset_873150_6.txt").read_text().split("\n")[:-1]
    g = defaultdict(list)
    for line in lines:
        v, neighbors_str = line.split(":")
        for w in neighbors_str.strip().split():
            g[v].append(w)
            if w not in g:
                g[w] = []
    print(" ".join(eulerian_path(g)))
