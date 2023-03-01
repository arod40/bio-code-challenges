from itertools import product

from fitting_alignment_problem import is_edge_down
from global_alignment_problem import build_graph_from_scores, path_to_alignment
from longest_path_dag import longest_path_dag


def is_edge_right(n1, n2):
    i1, j1 = n1
    i2, j2 = n2
    return j2 > j1 and i1 == i2


if __name__ == "__main__":
    match, mu, sigma = map(int, input().split())
    w1, w2 = input(), input()
    n1, n2 = len(w1), len(w2)

    s, t = (0, 0), (n1, n2)
    g = build_graph_from_scores(w1, w2, match, mu, sigma)
    # free-taxi edges, only where appropriate according to the overlap alignment definition
    # this is: you can skip any prefix of w1 or suffix from w2 with zero cost
    for i in range(n1 + 1):
        g[s].append(((i, 0), 0))
    for j in range(n2 + 1):
        g[n1, j].append((t, 0))

    nodes = [
        (i, j) for i, j in product(range(n1 + 1), range(n2 + 1))
    ]  # topological sort of nodes in the aligmnent matrix

    length, path = longest_path_dag(g, (0, 0), (n1, n2), nodes)

    # removing start and end nodes if free-taxi edge was used
    start_index = 0
    end_index = len(path)
    if is_edge_down(path[0], path[1]):
        start_index += 1
    if is_edge_right(path[-2], path[-1]):
        end_index -= 1

    print(length)

    w1_align, w2_align = path_to_alignment(path[start_index:end_index], w1, w2)

    print("".join(w1_align))
    print("".join(w2_align))
