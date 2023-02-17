from hamming_distance import hamming_distance


def approx_pattern_count(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i : i + len(pattern)], pattern) <= d:
            count += 1
    return count


if __name__ == "__main__":
    pattern = input()
    text = input()
    d = int(input())
    print(approx_pattern_count(text, pattern, d))
