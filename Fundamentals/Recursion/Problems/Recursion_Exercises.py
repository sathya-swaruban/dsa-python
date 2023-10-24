# 3.
def rec_countdown(n):
    """Prints the numbers from n to 0."""
    if n == 0:
        return 0
    elif n < 0:
        print(n)
        return rec_countdown(n + 1)
    else:
        print(n)
        return rec_countdown(n - 1)


# Tests
print(rec_countdown(5))
print(rec_countdown(0))
print(rec_countdown(-2))


# 4.
def rec_countup(n, j):
    """Counts up to n from 0."""
    if j == n:
        return n
    elif n < 0:
        print(j)
        return rec_countup(n, j - 1)
    else:
        print(j)
        return rec_countup(n, j + 1)


# Tests
print(rec_countup(5, 0))
print(rec_countup(0, 0))
print(rec_countup(-2, 0))


# 5.
def rec_reverse_string(input_string):
    """Reverse the input string using recursion."""
    if len(input_string) == 0:
        return ""
    else:
        return input_string[-1] + rec_reverse_string(input_string[:-1])


# Tests
assert rec_reverse_string("Sarina") == "aniraS"
assert rec_reverse_string("") == ""
assert rec_reverse_string("A") == "A"


# 6.
def rec_is_prime(m):
    """Uses recursion to check if m is prime."""
    def prime_helper(n, j):
        """Helper Function to iterate through all j less than m up to 1 to look for even divisors."""
        if j == 1:  # Assume 1 is a prime number even though it's debatable.
            return True
        else:
            return n % j != 0 and prime_helper(n, j - 1)
    return prime_helper(m, m - 1)


# Tests
assert rec_is_prime(5)
assert not rec_is_prime(6)


# 7.
def rec_fib(n):
    """Returns the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


assert rec_fib(3) == 2
assert rec_fib(4) == 3
