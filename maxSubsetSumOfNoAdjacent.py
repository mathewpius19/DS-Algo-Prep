def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first


print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))
