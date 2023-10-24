"""
Exercise-06:
    Write a function using recursion to check if a number n is prime.
    NOTE: You have to check whether n is divisible by any number below n.
"""


def rec_is_prime(m):
    def prime_helper(n, j):
        # Helper Function to iterate through all j less than m up to 1 to look for even divisors.
        if j == 1:  # Base case. (Assume 1 is a prime number even though it's debatable)
            return True
        else:  # Recursive case.
            return n % j != 0 and prime_helper(n, j - 1)
    return prime_helper(m, m - 1)


# Tests
if __name__ == '__main__':
    print(rec_is_prime(5))
