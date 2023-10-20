# Linear Search using iterative method
# Time Complexity: O(n)
# Space Complexity: O(1)
def linear_search_i(numbers, element):
    for i in range(len(numbers)):
        if numbers[i] == element:
            return i
    return -1


# Linear Search using recursive method
# Time Complexity: O(n)
# Space Complexity: O(1)
def linear_search_r(numbers, size, element):
    if size == 0:
        return -1
    elif numbers[size - 1] == element:
        return size - 1
    return linear_search_r(numbers, size - 1, element)


if __name__ == '__main__':
    result1 = linear_search_i([18, 12, 9, 14, 77, 50], 14)
    print(result1)

    result2 = linear_search_r([18, 12, 9, 14, 77, 50], 6, 14)
    print(result2)
