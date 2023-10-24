"""
Exercise-03:
    Write a function using recursion to print numbers from n to 0.
"""


def rec_countdown(n):
    if n == 0:  # Base case.
        return 0
    elif n < 0:  # Recursive case if n is negative number
        print(n)
        return rec_countdown(n + 1)
    else:  # Recursive case if n is positive number
        print(n)
        return rec_countdown(n - 1)


# Tests
if __name__ == '__main__':
    print(rec_countdown(5))
