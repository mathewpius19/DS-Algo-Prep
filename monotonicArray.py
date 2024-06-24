def isMonotonic(array):
    # Write your code here.
    if len(array) == 0 or len(array) == 1:
        return True
    monotonicInc = True
    monotonicDec = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            monotonicInc = False
            break
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            monotonicDec = False
            break
    if monotonicDec or monotonicInc:
        return True
    else:
        return False


print(isMonotonic([-1, -5, 10, -900, -1100, -1101, -1102, -9001]))
