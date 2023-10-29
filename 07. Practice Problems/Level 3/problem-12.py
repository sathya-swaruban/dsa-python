# lex_auth_012751752635383808104
"""
TODO: Problem Statement goes here
"""


def count_ways(n):
    if n == 1:
        return 4
    count_b = 1
    count_s = 1
    for i in range(2, n + 1):
        prev_count_b = count_b
        prev_count_s = count_s
        count_s = prev_count_b + prev_count_s
        count_b = prev_count_s
    result = count_s + count_b
    return result * result


if __name__ == '__main__':
    number = 5
    print("Number of possible ways in which buildings can be constructed is: ", count_ways(number))
