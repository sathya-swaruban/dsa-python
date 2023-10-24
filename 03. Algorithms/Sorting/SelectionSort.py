# Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        k = i + 1
        for j in range(k + 1, len(numbers)):
            if numbers[k] > numbers[j]:
                k = j + 1
        if numbers[i] > numbers[k]:
            numbers[i], numbers[k] = numbers[k], numbers[i]


if __name__ == '__main__':
    numbers_list = [8, 2, 19, 34, 23, 67, 91]
    print('Before Selection Sort : ', numbers_list)
    selection_sort(numbers_list)
    print('After Selection Sort : ', numbers_list)
