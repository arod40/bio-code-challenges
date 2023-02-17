def reverse_complement(s):
    compl = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join([compl[c] for c in s[::-1]])


if __name__ == "__main__":
    s = input()
    print(reverse_complement(s))
