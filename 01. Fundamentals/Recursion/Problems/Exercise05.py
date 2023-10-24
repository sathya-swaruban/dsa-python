"""
Exercise-05:
    Write a function using recursion that takes in a string and returns a reversed copy of the string.
    NOTE: The only string operation you are allowed to use is string concatenation.
"""


def rec_reverse_string(input_string):
    if len(input_string) == 0:  # Base case.
        return ''
    else:  # Recursive case.
        return input_string[-1] + rec_reverse_string(input_string[:-1])


# Tests
if __name__ == '__main__':
    print(rec_reverse_string('Python'))
