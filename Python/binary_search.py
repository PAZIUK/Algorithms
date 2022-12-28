my_array = [1, 3, 5, 7, 9]


def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high)
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(my_array, 3))
