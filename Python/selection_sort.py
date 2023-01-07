not_sorted = [-3, 5, 0, -8, 1, 10]


def selection_sort(array: list) -> list:                        # Sort (min -> max)
    for run in range(len(array) - 1):
        for i in range(run + 1, len(array)):                    # Search min value
            if array[i] < array[run]:
                array[i], array[run] = array[run], array[i]     # Value exchange

    return array


def selection_sort_reverse(array: list) -> list:                # Sort (max -> min)
    for run in range(len(array) - 1):
        for i in range(run + 1, len(array)):                    # Search max value
            if array[i] > array[run]:
                array[i], array[run] = array[run], array[i]     # Value exchange

    return array


print(f"Sorted array from min to max: {selection_sort(not_sorted)}")
print(f"Sorted array from max to min: {selection_sort_reverse(not_sorted)}")
