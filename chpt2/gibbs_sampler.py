from greedy_motif_search import compute_score_of_motifs
from greedy_motif_search_with_pseudocounts import compute_profile_mat_with_pseudocounts
from numpy.random import choice, randint
from profile_most_probable import kmer_probability
from randomized_motif_search import randomly_select_kmers


def profile_randomly_generated_kmer(text, profile_matrix):
    kmers = [text[i : i + k] for i in range(len(text) - k + 1)]
    weights = [kmer_probability(kmer, profile_matrix) for kmer in kmers]
    total = sum(weights)
    probs = [weight / total for weight in weights]
    return choice(kmers, 1, p=probs)[0]


def gibbs_sampler(dna, k, t, N):
    motifs = randomly_select_kmers(dna, k)
    best_motifs = motifs
    best_score = compute_score_of_motifs(best_motifs)
    for _ in range(N):
        i = randint(t)
        profile_matrix = compute_profile_mat_with_pseudocounts(
            motifs[:i] + motifs[i + 1 :], k
        )
        motifs[i] = profile_randomly_generated_kmer(dna[i], profile_matrix)
        motifs_score = compute_score_of_motifs(motifs)
        if motifs_score < best_score:
            best_score = motifs_score
            best_motifs = motifs.copy()
    return best_motifs, best_score


if __name__ == "__main__":
    k, t, N = map(int, input().split())
    dna = input().split()

    from math import inf

    from tqdm import tqdm

    best_score = inf
    for _ in tqdm(range(30)):
        motifs, score = gibbs_sampler(dna, k, t, N)
        if score < best_score:
            best_motifs = motifs
            best_score = score
    print(" ".join(best_motifs))
