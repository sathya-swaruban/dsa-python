# lex_auth_012751757069950976107
"""
TODO: Problem Statement goes here
"""


def find_optimal(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(i - 2):
            dp[i] = max(dp[i], dp[j] * (i - j - 1))
    return dp[n]


if __name__ == '__main__':
    print(find_optimal(7))
