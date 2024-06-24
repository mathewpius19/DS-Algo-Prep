def sortSubarray(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(num, i, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == float("inf"):
        return [-1, -1]
    leftSubarrayIdx = 0
    while minOutOfOrder >= array[leftSubarrayIdx]:
        leftSubarrayIdx += 1
    rightSubarrayIdx = len(array) - 1
    while maxOutOfOrder <= array[rightSubarrayIdx]:
        rightSubarrayIdx -= 1
    return [leftSubarrayIdx, rightSubarrayIdx]


def isOutOfOrder(num, i, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]


print(sortSubarray([-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]))
