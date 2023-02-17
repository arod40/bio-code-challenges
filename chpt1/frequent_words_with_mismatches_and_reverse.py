from frequent_words_with_mismatches import neighbors
from reverse_complement import reverse_complement

def compute_freq_map_with_mismatches_and_reverse(text, k, d):
    freq_map = {}
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        for neighbor in neighbors(pattern, d):
            freq_map[neighbor] = freq_map.get(neighbor, 0) + 1
        for neighbor in neighbors(reverse_complement(pattern), d):
            freq_map[neighbor] = freq_map.get(neighbor, 0) + 1
    return freq_map


def frequent_words_with_mismatches_and_reverse(text, k, d):
    freq_map = compute_freq_map_with_mismatches_and_reverse(text, k, d)
    max_count = max(freq_map.values())
    return [pattern for pattern, count in freq_map.items() if count == max_count]


if __name__ == "__main__":
    text = input()
    k, d = map(int, input().split())
    print(" ".join(frequent_words_with_mismatches_and_reverse(text, k, d)))
