from greedy_motif_search import compute_score_of_motifs
from profile_most_probable import profile_most_probable


def compute_profile_mat_with_pseudocounts(motifs, k):
    profile_mat = {
        "A": [1] * k,
        "C": [1] * k,
        "T": [1] * k,
        "G": [1] * k,
    }
    for j in range(k):
        for motif in motifs:
            current_base = motif[j]
            profile_mat[current_base][j] += 1
    return profile_mat


def greedy_motif_search_with_pseudocounts(dna, k, t):
    n = len(dna[0])
    best_motifs = [dnai[:k] for dnai in dna]
    best_score = compute_score_of_motifs(best_motifs)

    for j in range(n - k + 1):
        motifs = [dna[0][j : j + k]]
        for i in range(1, t):
            profile_matrix = compute_profile_mat_with_pseudocounts(motifs, k)
            motifs.append(profile_most_probable(dna[i], k, profile_matrix))

        motifs_score = compute_score_of_motifs(motifs)
        if motifs_score < best_score:
            best_score = motifs_score
            best_motifs = motifs

    return best_motifs


if __name__ == "__main__":
    k, t = map(int, input().split())
    dna = input().split()
    print(" ".join(greedy_motif_search_with_pseudocounts(dna, k, t)))
