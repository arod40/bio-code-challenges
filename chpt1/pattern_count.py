def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i : i + len(pattern)] == pattern:
            count += 1
    return count


if __name__ == "__main__":
    text = input()
    pattern = input()
    print(pattern_count(text, pattern))
