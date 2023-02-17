from hamming_distance import hamming_distance


def approx_pattern_matching(text, pattern, d):
    n, k = len(text), len(pattern)
    return [
        i for i in range(n - k + 1) if hamming_distance(text[i : i + k], pattern) <= d
    ]


if __name__ == "__main__":
    pattern = input()
    text = input()
    d = int(input())
    print(" ".join([str(x) for x in approx_pattern_matching(text, pattern, d)]))
