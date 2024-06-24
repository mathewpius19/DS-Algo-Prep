def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[j] == toMove:
            j -= 1
            continue
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array


print(moveElementToEnd([5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], 5))
