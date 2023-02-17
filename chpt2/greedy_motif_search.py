from profile_most_probable import profile_most_probable


def compute_score_of_motifs(motifs):
    k = len(motifs[0])
    profile_matrix = compute_profile_mat(motifs, k)
    return sum(
        [
            len(motifs)
            - max(
                profile_matrix["A"][j],
                profile_matrix["C"][j],
                profile_matrix["G"][j],
                profile_matrix["T"][j],
            )
            for j in range(k)
        ]
    )


def compute_profile_mat(motifs, k):
    profile_mat = {
        "A": [0] * k,
        "C": [0] * k,
        "T": [0] * k,
        "G": [0] * k,
    }
    for j in range(k):
        for motif in motifs:
            current_base = motif[j]
            profile_mat[current_base][j] += 1
    return profile_mat


def greedy_motif_search(dna, k, t):
    n = len(dna[0])
    best_motifs = [dnai[:k] for dnai in dna]
    best_score = compute_score_of_motifs(best_motifs)

    for j in range(n - k + 1):
        motifs = [dna[0][j : j + k]]
        for i in range(1, t):
            profile_matrix = compute_profile_mat(motifs, k)
            motifs.append(profile_most_probable(dna[i], k, profile_matrix))

        motifs_score = compute_score_of_motifs(motifs)
        if motifs_score < best_score:
            best_score = motifs_score
            best_motifs = motifs

    return best_motifs


if __name__ == "__main__":
    k, t = map(int, input().split())
    dna = input().split()
    print(" ".join(greedy_motif_search(dna, k, t)))
