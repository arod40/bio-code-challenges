def compute_freq_map(text, k):
    freq_map = {}
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        freq_map[pattern] = freq_map.get(pattern, 0) + 1
    return freq_map


def frequent_words(text, k):
    freq_map = compute_freq_map(text, k)
    max_count = max(freq_map.values())
    return [pattern for pattern, count in freq_map.items() if count == max_count]


if __name__ == "__main__":
    text = input()
    k = int(input())
    print(" ".join(frequent_words(text, k)))
