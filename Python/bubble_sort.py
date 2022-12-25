not_sorted = [5, 7, 4, 3, 8, 2]


def bubble_sort(array):
    for run in range(len(array) - 1):
        for i in range(len(array) - run - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


print(f"Sorted array: {bubble_sort(not_sorted)}")
