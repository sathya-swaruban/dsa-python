"""
Exercise-04:
    Write a function using recursion to print numbers from 0 to n.
    NOTE: You just need to change one line in the program of problem 3
"""


def rec_countup(n, j):
    if j == n:  # Base case.
        return n
    elif n < 0:  # Recursive case if n is negative number
        print(j)
        return rec_countup(n, j - 1)
    else:  # Recursive case if n is positive number
        print(j)
        return rec_countup(n, j + 1)


# Tests
if __name__ == '__main__':
    print(rec_countup(-5, 0))
