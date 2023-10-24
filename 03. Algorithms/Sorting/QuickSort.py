# Quick Sort
# Time Complexity: O(n^2)
# Space Complexity: O(log n)
def quick_sort(numbers, low, high):
    if low >= high:
        return
    split_point = partition(numbers, low, high)
    quick_sort(numbers, low, split_point - 1)
    quick_sort(numbers, split_point + 1, high)


def partition(numbers, low, high):
    pivot = numbers[low]
    i, j = low + 1, high
    is_done = False
    while not is_done:
        while i <= j and numbers[i] <= pivot:
            i += 1
        while numbers[j] >= pivot and j >= i:
            j -= 1
        if j < i:
            is_done = True
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[low], numbers[j] = numbers[j], numbers[low]
    return j


if __name__ == '__main__':
    numbers_list = [8, 2, 19, 34, 23, 67, 91]
    print('Before Quick Sort : ', numbers_list)
    quick_sort(numbers_list, 0, 6)
    print('After Quick Sort : ', numbers_list)
