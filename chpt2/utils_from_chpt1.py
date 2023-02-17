nucleotides = ["A", "G", "T", "C"]

def hamming_distance(p, q):
    return sum([a != b for a, b in zip(p, q)])

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return set(nucleotides)

    neighborhood = set()
    suffix_pattern = pattern[1:]
    suffix_neighborhood = neighbors(suffix_pattern, d)
    for text in suffix_neighborhood:
        if hamming_distance(text, suffix_pattern) < d:
            for n in nucleotides:
                neighborhood.add(n + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

def approx_pattern_matching(text, pattern, d):
    n, k = len(text), len(pattern)
    return [
        i for i in range(n - k + 1) if hamming_distance(text[i : i + k], pattern) <= d
    ]