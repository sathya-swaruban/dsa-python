"""
Exercise-01:
    Write a function that takes in two non-negative numbers and recursively multiplies them together.
"""


def rec_mult(num_1, num_2):
    if num_1 == 1:  # Base case.
        return num_2
    elif num_1 == 0:  # Deal with input case 0.
        return 0
    else:  # Recursive case.
        return num_2 + rec_mult(num_1 - 1, num_2)


# Tests
if __name__ == '__main__':
    print(rec_mult(5, 40))
