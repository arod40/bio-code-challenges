def manhattan_tourist(n, m, down, right):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + down[i - 1][0]
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + right[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(
                dp[i - 1][j] + down[i - 1][j], dp[i][j - 1] + right[i][j - 1]
            )
    return dp[n][m]


if __name__ == "__main__":
    n, m = map(int, input().split())
    down = []
    right = []
    for _ in range(n):
        down.append(list(map(int, input().split())))
    input()
    for _ in range(n + 1):
        right.append(list(map(int, input().split())))

    print(manhattan_tourist(n, m, down, right))
