def getPairDiff(array):
    pairs = set()
    for i in range(len(array)):
        for j in range(len(array)):
            pairs.add((array[i], array[j]))
    largest = float("-inf")
    for value in pairs:
        diff = getDiff(value)
        if diff > largest:
            largest = diff
    return largest


def getDiff(s):
    diff = 0
    for value in s:
        diff = abs(value - diff)
    return diff
    # return diff


s1 = set((2, 6))
print(getPairDiff([2, 6, 10]))
