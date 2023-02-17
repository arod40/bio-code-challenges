from frequent_words import compute_freq_map

def find_clumps(text, k, L, t):
    patterns = set()
    for i in range(len(text) - L + 1):
        freq_map = compute_freq_map(text[i : i + L], k)
        patterns.update([pattern for pattern, freq in freq_map.items() if freq >= t])
    return patterns


if __name__ == "__main__":
    text = input()
    k, L, t = map(int, input().split())
    print(" ".join(find_clumps(text, k, L, t)))
