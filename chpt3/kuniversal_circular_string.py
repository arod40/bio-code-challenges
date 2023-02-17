from de_bruijin_graph_from_kmers import de_brujin_graph
from eulerian_cycle import eulerian_cycle
from string_spelled_by_genome_path import string_spelled_by_genome_path


def get_all_binaries(k):
    for n in range(2**k):
        bits = []
        for _ in range(k):
            bit, n = n & 1, n >> 1
            bits.append(str(bit))
        yield "".join(bits)


def kuniversal_circular_string(k):
    kmers = list(get_all_binaries(k))
    g = de_brujin_graph(kmers)
    path = eulerian_cycle(g)
    return string_spelled_by_genome_path(path)[: -k + 1]


if __name__ == "__main__":
    k = int(input())
    print(kuniversal_circular_string(k))
