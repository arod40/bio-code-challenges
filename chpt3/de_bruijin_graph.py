from collections import defaultdict


def de_brujin_graph(dna, k):
    kmers = [dna[i : i + k] for i in range(len(dna) - k + 1)]
    g = defaultdict(list)
    for kmer in kmers:
        g[kmer[:-1]].append(kmer[1:])
    return g


if __name__ == "__main__":
    from pathlib import Path
    lines = Path("dataset_873146_6.txt").read_text().split()

    k = int(lines[0])
    dna = lines[1]

    elems = []
    for kmer, neighbors in de_brujin_graph(dna, k).items():
        if neighbors:
            elems.append(f"{kmer}: {' '.join(neighbors)}")

    Path("out.txt").write_text("\n".join(elems))
