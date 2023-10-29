# lex_auth_01275171950687846476
"""
Given the amount and denomination list, write a recursive python function to find and return the number of ways in which
the change can be provided for the specified amount using the given denomination list.

Assume that more than one note is available for each amount in the denomination list.

Example:
    - input:
        amount-10
        denomination_list-[10,5,1]
    - output:
        4
"""


def count_change(amount, coins):
    dp = [1] + [0] * amount
    for c in coins:
        for i in range(c, amount + 1):
            dp[i] += dp[i - c]
    return dp[amount]


if __name__ == '__main__':
    print(count_change(200, [50, 25, 10, 5, 2, 1]))
