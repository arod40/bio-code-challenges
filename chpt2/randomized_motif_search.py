from random import choice
from greedy_motif_search_with_pseudocounts import (
    compute_profile_mat_with_pseudocounts,
    compute_score_of_motifs,
)
from profile_most_probable import profile_most_probable


def calculate_motifs(profile_matrix, dna, k):
    motifs = []
    for text in dna:
        motifs.append(profile_most_probable(text, k, profile_matrix))
    return motifs


def randomly_select_kmers(dna, k):
    motifs = []
    for line in dna:
        n = len(line) - k + 1
        start = choice(range(n))
        motifs.append(line[start : start + k])
    return motifs


def randomized_motif_search(dna, k, t):
    motifs = randomly_select_kmers(dna, k)
    best_motifs = motifs
    best_score = compute_score_of_motifs(best_motifs)

    while True:
        profile_mat = compute_profile_mat_with_pseudocounts(motifs, k)
        motifs = calculate_motifs(profile_mat, dna, k)
        motifs_score = compute_score_of_motifs(motifs)
        if motifs_score < best_score:
            best_motifs = motifs
            best_score = motifs_score
        else:
            return best_motifs, best_score


if __name__ == "__main__":
    k, t = map(int, input().split())
    dna = input().split()

    from math import inf
    from tqdm import tqdm

    best_score = inf

    for _ in tqdm(range(1000)):
        motifs, score = randomized_motif_search(dna, k, t)
        if score < best_score:
            best_motifs = motifs
            best_score = score

    print(" ".join(best_motifs))
