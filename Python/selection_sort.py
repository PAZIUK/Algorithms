not_sorted = [-3, 5, 0, -8, 1, 10]


def selection_sort(array):
    for run in range(len(array) - 1):
        min_elem = array[run]               # Minimal value
        min_index = run                     # Index of minimal value
        
        for i in range(run + 1,len(array)): # Search minimal value
            if min_elem > array[i]:
                min_elem = array[i]
                min_index = i
                
        if min_index != run:                # Value exchange
            array[run], array[min_index] = array[min_index], array[run]
            
    return array


print(f"Sorted array: {selection_sort(not_sorted)}")
