def overlap_graph(kmers):
    return {
        kmer1: [kmer2 for kmer2 in kmers if kmer1[1:] == kmer2[:-1]] for kmer1 in kmers
    }


if __name__ == "__main__":
    from pathlib import Path

    kmers = Path("dataset_873145_10.txt").read_text().split()

    elems = []
    for kmer, neighbors in overlap_graph(kmers).items():
        if neighbors:
            elems.append(f"{kmer}: {' '.join(neighbors)}")
    
    Path("a.txt").write_text("\n".join(elems))
