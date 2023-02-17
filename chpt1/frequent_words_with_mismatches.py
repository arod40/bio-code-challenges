from hamming_distance import hamming_distance

nucleotides = ["A", "G", "T", "C"]


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


def compute_freq_map_with_mismatches(text, k, d):
    freq_map = {}
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        for neighbor in neighbors(pattern, d):
            freq_map[neighbor] = freq_map.get(neighbor, 0) + 1
    return freq_map


def frequent_words_with_mismatches(text, k, d):
    freq_map = compute_freq_map_with_mismatches(text, k, d)
    max_count = max(freq_map.values())
    return [pattern for pattern, count in freq_map.items() if count == max_count]


if __name__ == "__main__":
    text = input()
    k, d = map(int, input().split())
    print(" ".join(frequent_words_with_mismatches(text, k, d)))
    # print(" ".join(neighbors(text, d)))
