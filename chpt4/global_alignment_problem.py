from longest_path_dag import longest_path_dag
from itertools import product


def path_to_alignment(path, w1, w2):
    w1_align, w2_align = [], []
    posi, posj = path[0]
    for i, j in path[1:]:
        if i - posi == 1:
            w1_align.append(w1[posi])
        else:
            w1_align.append("-")
        if j - posj == 1:
            w2_align.append(w2[posj])
        else:
            w2_align.append("-")
        posi = i
        posj = j
    return w1_align, w2_align


def build_graph_from_scores(w1, w2, match, mu, sigma):
    n1, n2 = len(w1), len(w2)
    g = {}

    for i, j in product(range(n1 + 1), range(n2 + 1)):
        g[i, j] = []
        if i + 1 <= n1 and j + 1 <= n2:  # diagonal edge
            g[i, j].append(((i + 1, j + 1), match if w1[i] == w2[j] else -mu))
        if i + 1 <= n1:  # vertical edge
            g[i, j].append(((i + 1, j), -sigma))
        if j + 1 <= n2:  # horizontal edge
            g[i, j].append(((i, j + 1), -sigma))
    return g


if __name__ == "__main__":
    match, mu, sigma = map(int, input().split())
    w1, w2 = input(), input()
    n1, n2 = len(w1), len(w2)

    g = build_graph_from_scores(w1, w2, match, mu, sigma)
    nodes = [
        (i, j) for i, j in product(range(n1 + 1), range(n2 + 1))
    ]  # topological sort of nodes in the aligmnent matrix

    length, path = longest_path_dag(g, (0, 0), (n1, n2), nodes)
    print(length)

    w1_align, w2_align = path_to_alignment(path, w1, w2)

    print("".join(w1_align))
    print("".join(w2_align))
