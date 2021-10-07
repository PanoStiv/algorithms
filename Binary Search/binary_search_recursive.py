def binary_search(array, x, start, finish):
    middle = (start + finish) // 2

    if start <= finish:
        if x == array[middle]:
            return middle
        elif x < array[middle]:
            return binary_search(array, x, start,     middle-1)
        else: # x > array[middle]
            return binary_search(array, x, middle+1, finish)
    else:
        return -1