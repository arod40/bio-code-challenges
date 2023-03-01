from math import inf


def dp_change(money, coins):
    dp = [0]
    for m in range(1, money + 1):
        dp.append(inf)
        for coin in coins:
            if m >= coin:
                dp[m] = min(dp[m - coin] + 1, dp[m])
    return dp[money]


if __name__ == "__main__":
    money = int(input())
    coins = list(map(int, input().split()))

    print(dp_change(money, coins))
