# Merge Sort
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def merge(left_list, right_list):
    i, j = 0, 0
    sorted = list()
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            sorted.append(left_list[i])
            i += 1
        else:
            sorted.append(right_list[j])
            j += 1
    sorted.extend(left_list[i:])
    sorted.extend(right_list[j:])
    return sorted


def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    mid = len(num_list) // 2
    left_list = num_list[:mid]
    right_list = num_list[mid:]
    return merge(merge_sort(left_list), merge_sort(right_list))


if __name__ == '__main__':
    numbers_list = [8, 2, 19, 34, 23, 67, 91]
    print('Before Merge Sort : ', numbers_list)
    sorted_list = merge_sort(numbers_list)
    print('After Merge Sort : ', sorted_list)
