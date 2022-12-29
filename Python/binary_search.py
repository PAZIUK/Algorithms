import math

int_array = [1, 3, 5, 7, 9]
str_array = ['Bogdan', 'Dionisii', 'Oleksandr', 'Serhii', 'Stanislav']


def binary_search(array, item):             # Number binary search

    low = 0                                 # Low limit
    high = len(array) - 1                   # High limit

    while low <= high:
        mid = math.ceil((low + high) / 2)   # Get middle element index
        guess = array[mid]                  # Get middle element

        if guess == item:                   # Value found
            return mid                      # Return value index

        if guess > item:                    # Much
            high = mid - 1                  # Change high limit

        else:                               # Less
            low = mid + 1                   # Change low limit

    return None                             # Value doesn't exist


print(binary_search(int_array, 3))
print(binary_search(str_array, 'Serhii'))
