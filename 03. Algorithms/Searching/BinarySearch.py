# Binary Search using iterative method
# Time Complexity: O(log n)
# Space Complexity: O(1)
def binary_search_i(numbers, element):
    low, high = 0, len(numbers) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if numbers[middle] == element:
            return middle
        elif numbers[middle] < element:
            low = middle + 1
        elif numbers[middle] > element:
            high = middle - 1
    return -1


# Binary Search using recursive method
# Time Complexity: O(log n)
# Space Complexity: O(log n)
def binary_search_r(numbers, element, low, high):
    middle = (low + high) // 2
    if low <= high:
        if numbers[middle] == element:
            return middle
        elif numbers[middle] < element:
            return binary_search_r(numbers, element, middle + 1, high)
        elif numbers[middle] > element:
            return binary_search_r(numbers, element, low, middle - 1)
    else:
        return -1


# Order-Agnostic Binary Search using iterative method
# Time Complexity: O(log n)
# Space Complexity: O(1)
def binary_search_oa_i(numbers, element):
    low, high = 0, len(numbers) - 1
    is_ascending = numbers[low] < numbers[high]
    while low <= high:
        middle = low + (high - low) // 2
        if numbers[middle] == element:
            return middle
        if is_ascending:
            if numbers[middle] < element:
                low = middle + 1
            else:
                high = middle - 1
        else:
            if numbers[middle] > element:
                low = middle + 1
            else:
                high = middle - 1
    return -1


# Order-Agnostic Binary Search using recursive method
# Time Complexity: O(log n)
# Space Complexity: O(log n)
def binary_search_oa_r(numbers, element, low, high):
    is_ascending = numbers[low] < numbers[high]
    if low <= high:
        middle = (low + high) // 2
        if numbers[middle] == element:
            return middle
        if is_ascending:
            if numbers[middle] < element:
                return binary_search_oa_r(numbers, element, middle + 1, high)
            else:
                return binary_search_oa_r(numbers, element, low, middle - 1)
        else:
            if numbers[middle] > element:
                return binary_search_oa_r(numbers, element, middle + 1, high)
            else:
                return binary_search_oa_r(numbers, element, low, middle - 1)
    else:
        return -1


if __name__ == '__main__':
    result1 = binary_search_i([9, 12, 14, 18, 50, 77], 14)
    print(result1)

    result2 = binary_search_r([9, 12, 14, 18, 50, 77], 14, 0, 5)
    print(result2)

    result3 = binary_search_oa_i([77, 50, 18, 14, 12, 9], 14)
    print(result3)

    result3 = binary_search_oa_r([77, 50, 18, 14, 12, 9], 14, 0, 5)
    print(result3)
