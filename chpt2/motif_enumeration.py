from utils_from_chpt1 import neighbors, approx_pattern_matching


def motif_enumeration(dna, k, d):
    patterns = set()
    for i in range(len(dna[0]) - k + 1):
        kmer = dna[0][i : i + k]
        for neighbor in neighbors(kmer, d):
            if all(
                [
                    len(approx_pattern_matching(sub_dna, neighbor, d)) > 0
                    for sub_dna in dna
                ]
            ):
                patterns.add(neighbor)
    return patterns


if __name__ == "__main__":
    k, d = map(int, input().split())
    dna = input().split()
    print(" ".join(motif_enumeration(dna, k, d)))
