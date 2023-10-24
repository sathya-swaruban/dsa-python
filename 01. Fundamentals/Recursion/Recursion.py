def rec_sum(a_list):
    # Recursive sum
    if not a_list:
        # Base case: if a_list is empty, we have nothing more to add
        return 0
    else:
        # Recursive case
        return a_list[0] + rec_sum(a_list[1:])


def fact(n):
    # Recursive factorial definition
    if n < 0:
        # Just a check to make sure we don't call (-n)!
        return "Error - cannot accept neg numbers."
    elif n == 0:
        # Base case: 0! = 1
        return 1
    else:
        # Recursive case: n! = n*(n-1)!
        return n * fact(n - 1)


if __name__ == '__main__':
    print(rec_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(fact(5))
