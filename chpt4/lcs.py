DOWN = "down"
RIGHT = "right"
DIAG = "diag"


def output_lcs(backtrack, s, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == DOWN:
        return output_lcs(backtrack, s, i - 1, j)
    elif backtrack[i][j] == RIGHT:
        return output_lcs(backtrack, s, i, j - 1)
    else:
        return output_lcs(backtrack, s, i - 1, j - 1) + s[i - 1]


def lcs(s, t):
    n = len(s)
    m = len(t)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    backtrack = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = int(s[i - 1] == t[j - 1])
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + match)

            if dp[i][j] == dp[i - 1][j]:
                backtrack[i][j] = DOWN
            elif dp[i][j] == dp[i][j - 1]:
                backtrack[i][j] = RIGHT
            else:
                backtrack[i][j] = DIAG
    return output_lcs(backtrack, s, n, m)


if __name__ == "__main__":
    import sys

    sys.setrecursionlimit(2000)
    s, t = input(), input()
    print(lcs(s, t))
