# KMP algorithm for efficient pattern matching
# Reviewed and adapted the code from https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

def kmp(text, pattern):
    pi = calc_pi(pattern)

    k = 0
    q = 0
    while q < len(text):
        if pattern[k] == text[q]:
            q += 1
            k += 1

        if k == len(pattern):
            yield q - k
            k = pi[k - 1]

        elif q < len(text) and pattern[k] != text[q]:
            if k != 0:
                k = pi[k - 1]
            else:
                q += 1


def calc_pi(pattern):
    pi = [0] * len(pattern)
    k = 0
    q = 1

    while q < len(pattern):
        if pattern[q] == pattern[k]:
            k += 1
            pi[q] = k
            q += 1
        else:
            if k != 0:
                k = pi[k - 1]
            else:
                pi[q] = 0
                q += 1

    return pi


if __name__ == "__main__":
    pattern = input()
    text = input()
    print(" ".join([str(x) for x in kmp(text, pattern)]))
