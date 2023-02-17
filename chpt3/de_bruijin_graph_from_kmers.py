from collections import defaultdict
from tqdm import tqdm


def de_brujin_graph(kmers):
    g = {**{kmer[:-1]: [] for kmer in kmers}, **{kmer[1:]: [] for kmer in kmers}}
    for kmer in kmers:
        g[kmer[:-1]].append(kmer[1:])
    return g


if __name__ == "__main__":
    from pathlib import Path

    kmers = Path("dataset_873147_8.txt").read_text().split()

    elems = []
    for kmer, neighbors in de_brujin_graph(kmers).items():
        if neighbors:
            elems.append(f"{kmer}: {' '.join(neighbors)}")

    Path("out.txt").write_text("\n".join(elems))
