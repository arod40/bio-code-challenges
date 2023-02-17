def find_skews(text):
    m = {"G": 1, "C": -1, "A": 0, "T": 0}
    skews = [0]
    positions = []
    min_skew = len(text)
    for i, c in enumerate(text):
        skews.append(skews[-1] + m[c])
        if skews[-1] < min_skew:
            min_skew = skews[-1]
            positions = [i + 1]
        elif skews[-1] == min_skew:
            positions.append(i + 1)

    return positions


if __name__ == "__main__":
    text = input()
    print(" ".join([str(x) for x in find_skews(text)]))
