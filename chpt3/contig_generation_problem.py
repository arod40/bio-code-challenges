from de_bruijin_graph_from_kmers import de_brujin_graph
from string_spelled_by_genome_path import string_spelled_by_genome_path


def maximal_path_from_node(g, indegree, outdegree, node):
    # For each of the node's out-neighbors we can create a different contig
    for second in g[node]:
        path = [node]
        current = second
        while indegree[current] == outdegree[current] == 1:
            path.append(current)
            current = g[current][0]
        path.append(current)
        yield path


def contig_generation(kmers):
    g = de_brujin_graph(kmers)

    indegrees = {v: 0 for v in g}
    outdegrees = {v: 0 for v in g}

    for v in g:
        for w in g[v]:
            indegrees[w] += 1
            outdegrees[v] += 1

    for node in g:
        if indegrees[node] == 0 or indegrees[node] != 1 or outdegrees[node] != 1:
            for contig_path in maximal_path_from_node(g, indegrees, outdegrees, node):
                yield string_spelled_by_genome_path(contig_path)


if __name__ == "__main__":
    from pathlib import Path

    kmers = Path("dataset_873152_5.txt").read_text().split()
    print(" ".join(contig_generation(kmers)))
