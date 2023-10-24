"""
Exercise-02:
   Write a function that takes in a base and an exp and recursively computes base^exp.
   Note: You are not allowed to use the ** operator!
"""


def rec_expo(base, exp):
    if exp == 0:  # Base case.
        return 1
    else:  # Recursive case.
        return base * rec_expo(base, exp - 1)


# Tests
if __name__ == '__main__':
    print(rec_expo(0, 5))
    print(rec_expo(2, 4))
    print(rec_expo(3, 0))
