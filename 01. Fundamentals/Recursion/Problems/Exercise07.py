"""
Exercise-07:
    Write a recursive function that takes in one argument n and computes F(n), the n-th value of the Fibonacci sequence.
    NOTE: The Fibonacci sequence is defined by the relation F(n) = F(n−1) + F(n−2) where F(0) = 0 and F(1) = 1.
"""


def rec_fib(n):
    if n == 0:  # Base case 1.
        return 0
    elif n == 1:  # Base case 2.
        return 1
    else:  # Recursive case.
        return rec_fib(n - 1) + rec_fib(n - 2)


# Tests
if __name__ == '__main__':
    print(rec_fib(6))
