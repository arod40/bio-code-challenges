from de_bruijin_graph_from_kmers import de_brujin_graph
from eulerian_path import eulerian_path
from string_spelled_by_genome_path import string_spelled_by_genome_path


def string_reconstruction(kmers):
    g = de_brujin_graph(kmers)
    path = eulerian_path(g)
    return string_spelled_by_genome_path(path)


if __name__ == "__main__":
    from pathlib import Path

    lines = Path("dataset_873150_7.txt").read_text().splitlines()
    kmers = lines[1].split()

    print(string_reconstruction(kmers))
