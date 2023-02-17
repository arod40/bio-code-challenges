from math import inf
from utils_from_chpt1 import hamming_distance


def int2kmer(n, k):
    bit2base = {
        (0, 0): "A",
        (0, 1): "C",
        (1, 0): "G",
        (1, 1): "T",
    }
    bases = []
    for _ in range(k):
        a, b = n & 1, (n >> 1) & 1
        bases.append(bit2base[a, b])
        n = n >> 2
    return "".join(bases)


# iterating all integers up to the number of kmers we want to generate
# each number will be then converted to a unique motif using bitmask
def all_kmers(k):
    for n in range(4**k):
        yield int2kmer(n, k)


# this function serves both definitions of the
# mathematical function 'd' described in the book
def d(pattern, text):
    n = len(text)
    k = len(pattern)
    if isinstance(text, list):
        return sum(d(pattern, line) for line in text)
    elif isinstance(text, str):
        return min(hamming_distance(pattern, text[i : i + k]) for i in range(n - k + 1))


def median_string(dna, k):
    return min((d(pattern, dna), pattern) for pattern in all_kmers(k))[1]


if __name__ == "__main__":
    k = int(input())
    dna = input().split()
    print(median_string(dna, k))
