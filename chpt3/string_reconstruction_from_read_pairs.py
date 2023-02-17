from string_spelled_by_genome_path import string_spelled_by_genome_path
from eulerian_path import eulerian_path


def string_spelled_by_gapped_patterns(path, k, d):
    prefix_kmers = [pre for pre, _ in path]
    suffix_kmers = [suf for _, suf in path]
    prefix_string = string_spelled_by_genome_path(prefix_kmers)
    suffix_string = string_spelled_by_genome_path(suffix_kmers)

    if prefix_string[k + d :] == suffix_string[: -k - d]:
        return prefix_string + suffix_string[-k - d :]
    return None


def paired_de_brujin_graph(kdmers):
    g = {
        **{(kmer1[:-1], kmer2[:-1]): [] for kmer1, kmer2 in kdmers},
        **{(kmer1[1:], kmer2[1:]): [] for kmer1, kmer2 in kdmers},
    }
    for kmer1, kmer2 in kdmers:
        g[(kmer1[:-1], kmer2[:-1])].append((kmer1[1:], kmer2[1:]))
    return g


def string_reconstruction_from_read_pairs(kdmers, k, d):
    g = paired_de_brujin_graph(kdmers)
    path = eulerian_path(g)
    return string_spelled_by_gapped_patterns(path, k, d)


if __name__ == "__main__":
    from pathlib import Path

    lines = Path("dataset_873151_16.txt").read_text().split("\n")
    k, d = map(int, lines[0].split())
    kdmers = [tuple(kdmer_str.split("|")) for kdmer_str in lines[1].split()]

    print(string_reconstruction_from_read_pairs(kdmers, k, d))
