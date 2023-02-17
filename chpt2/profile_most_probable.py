def kmer_probability(kmer, profile_matrix):
    prob = 1
    for j, nucleotide in enumerate(kmer):
        prob *= profile_matrix[nucleotide][j]
    return prob


def profile_most_probable(text, k, profile_matrix):
    best_prob = -1
    for i in range(len(text) - k + 1):
        kmer = text[i : i + k]
        kmer_prob = kmer_probability(kmer, profile_matrix)
        if kmer_prob > best_prob:
            best_prob = kmer_prob
            best_kmer = kmer
    return best_kmer


if __name__ == "__main__":
    text = input()
    k = int(input())
    profile_matrix = {nucleotide: [] for nucleotide in "ACGT"}
    for nucleotide in profile_matrix:
        profile_matrix[nucleotide] = list(map(float, input().split()))

    print(profile_most_probable(text, k, profile_matrix))
