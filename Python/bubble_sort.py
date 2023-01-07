not_sorted = [5, 7, 4, 3, 8, 2]


def bubble_sort(array: list) -> list:                           # Sort (min -> max)
    for run in range(len(array) - 1):
        for i in range(len(array) - run - 1):                   # Search max value (Bubble)
            if array[i] > array[i + 1]:                         # Value exchange
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


def bubble_sort_reverse(array: list) -> list:                   # Reverse sort (max -> min)
    for run in range(len(array) - 1):
        for i in range(len(array) - run - 1):                   # Search min value (Bubble)
            if array[i] < array[i + 1]:                         # Value exchange
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


print(f"Sorted array from min to max: {bubble_sort(not_sorted)}")
print(f"Sorted array from max to min: {bubble_sort_reverse(not_sorted)}")
