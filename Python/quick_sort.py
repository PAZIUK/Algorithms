not_sorted = [10, 5, 2, 3]


def quick_sort(array: list) -> list:                                # Sort (min -> max)
    if len(array) < 2:                                              # Base case
        return array
    else:                                                           # Recursive case
        pivot = array[0]                                            # Reference point

        less = [i for i in array[1:] if i <= pivot]                 # Subarray of values less than reference point

        greater = [i for i in array[1:] if i > pivot]               # Subarray of values greater than reference point

        return quick_sort(less) + [pivot] + quick_sort(greater)     # Partition


print(quick_sort(not_sorted))
