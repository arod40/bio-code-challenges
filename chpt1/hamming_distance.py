def hamming_distance(p, q):
    return sum([a != b for a, b in zip(p, q)])


if __name__ == "__main__":
    p = input()
    q = input()
    print(hamming_distance(p, q))
