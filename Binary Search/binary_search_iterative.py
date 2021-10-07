def binary_search(array, x):
    start = 0
    finish = len(array)-1

    while start <= finish:
        middle = (start + finish) // 2
        if array[middle] == x:
            return middle
        elif array[middle] > x:
            finish = middle - 1
        else:
            start = middle + 1
    else:
        return -1
