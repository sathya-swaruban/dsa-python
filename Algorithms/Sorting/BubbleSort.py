# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def bubble_sort(numbers):
    length = len(numbers)
    for i in range(length - 1):
        is_swapped = False
        for j in range(length - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                is_swapped = True
        if not is_swapped:
            break


if __name__ == '__main__':
    numbers_list = [8, 2, 19, 34, 23, 67, 91]
    print('Before Bubble Sort : ', numbers_list)
    bubble_sort(numbers_list)
    print('After Bubble Sort : ', numbers_list)
